
from rest_framework import routers

from api.views import VideoViewSet

router = routers.SimpleRouter()
router.register(r'videos', VideoViewSet)
urlpatterns = router.urls
