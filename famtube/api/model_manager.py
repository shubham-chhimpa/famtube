from api.models import Video


class VideoManager(object):

    def add_video(self, title, description, published_at, thumbnail_url, video_id):
        try:
            video = Video.objects.create(title=title,
                                         description=description,
                                         published_at=published_at,
                                         thumbnail_url=thumbnail_url,
                                         video_id=video_id)

            video.save()
            return video
        except Exception as e:
            return None

    def get_videos(self):
        try:
            videos = Video.objects.order_by('-published_at').all()

            return videos
        except Exception as e:
            return None
