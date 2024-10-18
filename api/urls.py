from django.urls import include, path
from rest_framework_nested import routers

from api import views

router = routers.SimpleRouter()
router.register(r'authors', views.AuthorViewSet)
books_router = routers.NestedSimpleRouter(router, r'authors', lookup='book')
books_router.register(r'books', views.BookViewSet, basename='author-books')
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(books_router.urls)),
]
