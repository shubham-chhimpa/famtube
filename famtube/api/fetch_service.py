import threading
import requests

from django.conf import settings

from api.model_manager import VideoManager


def youtube_service():
    print(f"{threading.current_thread()} thread started.")
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': 'cricket',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'type': 'video',
        'maxResult': 10
    }

    search_request = requests.get(url=search_url, params=params)

    if search_request.status_code == 200:
        json_response = search_request.json()
        items = json_response['items']
        for item in items:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            published_at = item["snippet"]["publishedAt"]
            thumbnail_url = item["snippet"]["thumbnails"]["default"]["url"]
            video_id = item["id"]["videoId"]
            video_manager = VideoManager()
            video_manager.add_video(video_id=video_id, title=title, description=description,
                                    thumbnail_url=thumbnail_url, published_at=published_at)

    if search_request.status_code == 400:
        '''
        if request results in 400, then new API_KEY should be picked up
        '''
        print(f"{settings.YOUTUBE_DATA_API_KEY} Expired.")
