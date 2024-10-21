# Routers provide an easy way of automatically determining the URL conf.

from django.urls import path
from rest_framework import routers

from api.views import ReadOnlyProxyView

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/', ReadOnlyProxyView.as_view(source='users/'), name='user-list'),
    path('users/<int:pk>/', ReadOnlyProxyView.as_view(source='users/%(pk)s'), name='user-list'),
]

# urlpatterns += router.urls
