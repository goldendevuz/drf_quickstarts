# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin


class UserSerializer(QueryFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'is_staff']
