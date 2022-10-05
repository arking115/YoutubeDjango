from django.core.management.base import BaseCommand

from youtubescraper.models import YoutubeLink, Data
from youtubescraper.scraper import Scraper


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Get all YoutubeLink objects from db
        youtube_link_objs = YoutubeLink.objects.all()
        scraper = Scraper()
        # Iterate over all objects
        for youtube_link_obj in youtube_link_objs:
            # for each youtube link get its info
            name, views = scraper.get_youtube_link_info(youtube_link_obj.link)

            # if the current youtube_link_obj doesn't have a name - update it
            if not youtube_link_obj.name:
                youtube_link_obj.name = name
                youtube_link_obj.save()

            # add new data_obj to db for
            data_obj = Data.objects.create(
                youtube_link=youtube_link_obj,
                views=views
            )

