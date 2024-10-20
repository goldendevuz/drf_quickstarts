# djangorestframework-rapidjson

Provides
[rapidjson](https://github.com/python-rapidjson/python-rapidjson)
support with parser and renderer.

## How to install

``` shell
pip install djangorestframework-rapidjson
```

## How to use

Update django rest framework config

``` python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_rapidjson.renderers.RapidJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_rapidjson.parsers.RapidJSONParser',
    )
}
```
