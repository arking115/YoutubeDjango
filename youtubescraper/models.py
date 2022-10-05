from django.db import models


# Create your models here.
class YoutubeLink(models.Model):
    link = models.URLField("Link")
    name = models.CharField("Name", max_length=200, null=True, blank=True)


class Data(models.Model):
    youtube_link = models.ForeignKey(YoutubeLink, on_delete=models.CASCADE)
    views = models.IntegerField("Views", default=0)
    updated = models.DateTimeField("Updated", auto_now=True)
