from atexit import register
from django.contrib import admin
from .models import YoutubeLink, Data, YoutubeChannel
# Register your models here.
class ytlink_adminsite(admin.ModelAdmin):
    model = YoutubeLink
    list_display = ["name", "channel", "link"]

admin.site.register(YoutubeLink, ytlink_adminsite)
admin.site.register(Data)
admin.site.register(YoutubeChannel)