# Async Django REST framework

**Async support for Django REST framework**

# Requirements

* Python 3.8+
* Django 4.1+

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Installation

Install using `pip`...

    pip install adrf

Add `'adrf'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'adrf',
]
```

# Async ViewSet

For viewsets, all handler methods must be async too.

views.py
```python
# ViewSets define the view behavior.
from django.contrib.auth.models import User
from adrf import viewsets

from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

urls.py
```python
# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
```

# Async Serializer

serializers.py

```python
# Serializers define the API representation.
from django.contrib.auth.models import User
from adrf import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
```

Documentation: https://github.com/em1208/adrf/

