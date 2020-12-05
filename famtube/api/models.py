from django.db import models


class Video(models.Model):
    """
        Model to cache Video Data
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=500)
    video_id = models.CharField(max_length=200, unique=True)
