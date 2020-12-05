from rest_framework import viewsets

from api.model_manager import VideoManager
from api.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
        API endpoint for videos.
    """
    video_manager = VideoManager()
    queryset = video_manager.get_videos()
    serializer_class = VideoSerializer
    permission_classes = []
