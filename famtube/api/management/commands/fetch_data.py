from django.core.management.base import BaseCommand
from api.fetch_service import youtube_service
import threading
import time
import schedule


class Command(BaseCommand):
    help = "Instantiate the youtube fetch job scheduler"

    @staticmethod
    def run_threaded(job_func):
        job_thread = threading.Thread(target=job_func)
        job_thread.start()

    def handle(self, *args, **options):
        schedule.every(60).seconds.do(Command.run_threaded, youtube_service)
        while 1:
            schedule.run_pending()
            time.sleep(1)
