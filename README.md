```Django Jazzmin documentation```: https://django-jazzmin.readthedocs.io/

Welcome to Jazzmin, intended as a drop-in app to jazz up your django admin site, with plenty of things you can easily customise, including a built-in UI customizer

### Installation

Install using `pip install django-jazzmin`

Add `jazzmin` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    'jazzmin',  # Add this before 'django.contrib.admin'
]
```

### Prevent django's templatetag not found issue

Add 'length_is' tag to templatetags.
```python
TEMPLATES = [
    {
        'OPTIONS': {
            # ...
            "builtins": ["config.templatetags.length_is"], # Add this line to options
        },
    },
]
```

### Access the Admin
Once you've done this, run your Django server:

`python manage.py runserver`

Now, go to the Django admin panel at http://localhost:8000/admin/ and you should see the updated, customized admin interface powered by Django Jazzmin.