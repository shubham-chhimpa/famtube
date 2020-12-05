from rest_framework import serializers

from api.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['title', 'description', 'published_at', 'thumbnail_url', 'video_id']
