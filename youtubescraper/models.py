
from django.db import models

# Create your models here.
class YoutubeLink(models.Model):
    link = models.URLField(max_length=200)
    name = models.CharField(default=None, max_length=50)

class Data(models.Model):
    youtube_link = models.ForeignKey(YoutubeLink, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)