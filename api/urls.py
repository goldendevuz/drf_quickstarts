# Routers provide an easy way of automatically determining the URL conf.
from os.path import basename

from django.urls import path
from rest_framework import routers

from api.views import TextAPIView

# router = routers.DefaultRouter()
# router.register(r'texts', TextAPIView)
# urlpatterns = router.urls

urlpatterns = [
    path('texts', TextAPIView.as_view())
]