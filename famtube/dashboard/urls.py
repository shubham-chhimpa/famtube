from django.urls import path
from dashboard.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
]
