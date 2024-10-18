# Serializers define the API representation.
from django.contrib.auth.models import User
from adrf import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']