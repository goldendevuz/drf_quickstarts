# Django REST Framework JSON CamelCase
[![PyPI Version](https://badge.fury.io/py/djangorestframework-camel-case.svg)](https://badge.fury.io/py/djangorestframework-camel-case)

**Camel case JSON support for Django REST framework.**

## Installation

At the command line:

```bash
$ pip install djangorestframework-camel-case
$ pip install drf-orjson-renderer
```

Add the render and parser to your Django settings file.

```python
# ...
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        # If you use MultiPartFormParser or FormParser, we also have a camel case version
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # Any other parsers
    ),
}
# ...
```

Add query param middleware to the Django settings file.

```python
# ...
MIDDLEWARE = [
    # Any other middleware
    'djangorestframework_camel_case.middleware.CamelCaseMiddleWare',
]
# ...
```

## Swapping Renderer

By default, the package uses `rest_framework.renderers.JSONRenderer`. If you want to use another renderer, the two possible options are:

- `drf_orjson_renderer.renderers.ORJSONRenderer`
- `drf_ujson.renderers.UJSONRenderer`
- `rest_framework.renderers.UnicodeJSONRenderer` for DRF < 3.0.

Specify the renderer in your Django settings file.

```python
# ...
JSON_CAMEL_CASE = {
    'RENDERER_CLASS': 'drf_orjson_renderer.renderers.ORJSONRenderer'
}
# ...
```

## Underscoreize Options

### No Underscore Before Number

As raised in [this comment](https://github.com/krasa/StringManipulation/issues/8#issuecomment-121203018), there are two conventions of snake case.

```text
# Case 1 (Package default)
v2Counter -> v_2_counter
fooBar2 -> foo_bar_2

# Case 2
v2Counter -> v2_counter
fooBar2 -> foo_bar2
```

By default, the package uses the first case. To use the second case, specify it in your Django settings file.

```python
REST_FRAMEWORK = {
    # ...
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    # ...
}
```

Alternatively, you can change this behavior on a class level by setting `json_underscoreize`:

```python
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework.generics import CreateAPIView

class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}

class MyView(CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    parser_classes = (NoUnderscoreBeforeNumberCamelCaseJSONParser,)
```