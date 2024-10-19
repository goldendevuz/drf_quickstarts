# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
