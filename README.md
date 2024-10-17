```Django Jazzmin documentation```: https://django-jazzmin.readthedocs.io/

Welcome to Jazzmin, intended as a drop-in app to jazz up your django admin site, with plenty of things you can easily customise, including a built-in UI customizer

### 1. Installation

Install using `pip install django-jazzmin`

Add `jazzmin` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    'jazzmin',  # Add this before 'django.contrib.admin'
]
```

### 2. Create the [templatetags](config/templatetags) directory and files
```shell
config/
    templatetags/
        __init__.py # Optional
        length_is.py
```

### 3. Define the [length_is](config/templatetags/length_is.py) tag
```python
from django import template

register = template.Library()


@register.filter(is_safe=False)
def length_is(value, arg):
    """Return a boolean of whether the value's length is the argument."""

    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ""
```

### 4. Register the 'length_is' tag in your `templatetags` module.

To make the custom `length_is` tag globally available across all apps, add it to your app's `templatetags` module and configure it in the `TEMPLATES` setting:

```python
TEMPLATES = [
    {
        'OPTIONS': {
            # ...
            'builtins': ['your_app.templatetags.custom_tags'],  # Add this line to OPTIONS
        },
    },
]
```

### 5. Access the Admin
Once you've done this, run your Django server:

`python manage.py runserver`

Now, go to the Django admin panel at http://localhost:8000/admin/ and you should see the updated, customized admin interface powered by Django Jazzmin.