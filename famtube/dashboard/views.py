from django.core.paginator import Paginator
from django.shortcuts import render

from api.model_manager import VideoManager


def home_page(request):
    video_manager = VideoManager()
    videos = video_manager.get_videos()
    paginator = Paginator(videos, 10)  # Show 10 videos per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/index.html', {'page_obj': page_obj})
