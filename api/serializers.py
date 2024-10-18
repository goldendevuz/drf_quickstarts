from rest_framework.serializers import ModelSerializer

from api.models import Author, Book, Chapter


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
