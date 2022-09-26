from django.core.management.base import BaseCommand
from youtubescraper.scraper import scraper

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(scraper('https://www.youtube.com/watch?v=V0RfgNIwCqI&t=434s'))