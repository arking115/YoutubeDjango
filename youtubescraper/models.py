from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class YoutubeChannel(models.Model):
    ch_link = models.URLField("Channel Link")
    ch_name = models.CharField("Channel Name", max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.pk) + " - " + self.ch_name


class YoutubeLink(models.Model):
    link = models.URLField("Link")
    name = models.CharField("Name", max_length=200, null=True, blank=True)
    channel = models.ForeignKey(YoutubeChannel, on_delete=models.CASCADE)


class Data(models.Model):
    youtube_link = models.ForeignKey(YoutubeLink, on_delete=models.CASCADE)
    views = models.IntegerField("Views", default=0)
    updated = models.DateTimeField("Updated", auto_now=True)
