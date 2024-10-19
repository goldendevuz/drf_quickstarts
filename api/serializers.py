from django.contrib.auth import get_user_model
from drf_compound_fields.fields import ListField, ListOrItemField, DictField, PartialDictField
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # This is the new stuff:
    phone_numbers = ListField(child=serializers.CharField(), allow_empty=True)
    skills = ListField(child=serializers.CharField(), allow_empty=True)  # E.g., ["javascript", "python", "ruby"]
    username = ListOrItemField(serializers.CharField())  # E.g., "Prince" or ["John", "Smith"]
    bookmarks = DictField(child=serializers.URLField(), allow_empty=True)  # E.g., {"./": "http://slashdot.org"}
    measurements = PartialDictField(child=serializers.IntegerField(), included_keys=['height', 'weight'])

    class Meta:
        model = User
        # fields = '__all__' # Not recommended for this model
        fields = ['id', 'username', 'email', 'phone_numbers', 'bookmarks', 'measurements', 'skills']
