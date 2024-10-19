from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_compound_fields.fields import ListField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    phone_numbers = ListField(child=serializers.CharField(), allow_empty=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_numbers']
