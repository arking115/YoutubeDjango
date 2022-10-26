from django.core.management.base import BaseCommand

from youtubescraper.models import YoutubeLink, YoutubeChannel
from youtubescraper.scraper import Scraper


class Command(BaseCommand):
    def handle(self, *args, **options):
        youtube_channel_objs = YoutubeChannel.objects.all()
        scraper = Scraper()
        yt_links = YoutubeLink.objects.all()
        #Saving the data links from YoutubeLink Table
        yt_links_url = []
        for yt_link in yt_links:
            yt_links_url.append(yt_link.link)

        #Searching through the existing db channels
        for youtube_channel_obj in youtube_channel_objs:
            yt_link_list = scraper.get_channel_videos(youtube_channel_obj.ch_link)
            for yot_link in yt_link_list:
                if not yot_link in yt_links_url:
                #Creating the new YoutubeLink objects for each individual links if it was not already added
                    data_obj = YoutubeLink.objects.create(
                        link=yot_link,
                        channel=youtube_channel_obj
                    )