# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_proxy.views import ProxyView

from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReadOnlyProxyView(ProxyView):
    http_method_names = ['get']
