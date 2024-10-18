from rest_framework import viewsets
from api.models import Author, Book, Chapter
from api.serializers import AuthorSerializer, BookSerializer, ChapterSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_pk = self.kwargs.get('author_pk')
        return Book.objects.filter(author__pk=author_pk)


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        book_pk = self.kwargs.get('book_pk')
        return Chapter.objects.filter(book__pk=book_pk)
