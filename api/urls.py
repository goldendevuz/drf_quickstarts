from django.urls import path

from api.views import TextAPIView

urlpatterns = [
    path('texts', TextAPIView.as_view())
]
