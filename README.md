# drf-nested-routers

This package provides routers and fields to create nested resources in the [Django Rest Framework](http://django-rest-framework.org/)

Nested resources are needed for full REST URL structure, if one resource lives inside another.

The following example is about Authors, Books and Chapters.
There are many authors, and each author has many books, each book has chapters. The "book" resource does not
exist without an author, and chapter without a book, so you need them "nested" inside the author.

## Installation

You can install this library using pip:

```pip install drf-nested-routers```

It is not needed to add this library in your Django project's `settings.py` file, as it does not contain any app, signal or model.

## Quickstart

### Infinite-depth Nesting

Example of nested router 3 levels deep.
You can use this same logic to nest routers as deep as you need.
This example ahead accomplishes the below URL patterns.
```
/authors/
/authors/{pk}/
/authors/{author_pk}/books/
/authors/{author_pk}/books/{pk}/
/authors/{author_pk}/books/{book_pk}/chapters/
/authors/{author_pk}/books/{book_pk}/chapters/{chapter_pk}/
```

```python
# urls.py
from rest_framework_nested import routers
from django.urls import path, include
from .views import AuthorViewSet, BookViewSet, ChapterViewSet

# Create the main router for Author
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)

# Create nested routers for Book under Author
books_router = routers.NestedDefaultRouter(router, r'authors', lookup='author')
books_router.register(r'books', BookViewSet, basename='author-books')

# Create nested routers for Chapter under Book
chapters_router = routers.NestedDefaultRouter(books_router, r'books', lookup='book')
chapters_router.register(r'chapters', ChapterViewSet, basename='book-chapters')

# Include the routers in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),
    path('', include(chapters_router.urls)),
]
```

```python
# views.py
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
```

```python
# serializers.py
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
```