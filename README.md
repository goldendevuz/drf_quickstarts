```Django Jazzmin``` documentation: https://django-jazzmin.readthedocs.io/

Welcome to Jazzmin, intended as a drop-in app to jazz up your django admin site, with plenty of things you can easily customise, including a built-in UI customizer

### Installation

Install using `pip install django-jazzmin`

Add `jazzmin` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    'jazzmin',  # Add this before 'django.contrib.admin'
]
```