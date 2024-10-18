from rest_framework import serializers

from api.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer to show book details

    class Meta:
        model = Author
        fields = '__all__'
