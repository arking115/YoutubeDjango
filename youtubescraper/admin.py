from atexit import register
from django.contrib import admin
from .models import YoutubeLink, Data
# Register your models here.
admin.site.register(YoutubeLink)
admin.site.register(Data)