# serializers.py
from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']  # Profile fields

class UserSerializer(serializers.ModelSerializer):
    # Set profile to be optional
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'profile']  # Include profile field in the output

    def create(self, validated_data):
        # Extract profile data if available
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create(**validated_data)

        if profile_data:
            Profile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        # Update user fields
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update profile if profile data is provided
        if profile_data:
            Profile.objects.update_or_create(user=instance, defaults=profile_data)

        return instance
