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
