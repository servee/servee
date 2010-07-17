from django.contrib import admin
from servee.contrib.media.video.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Video, VideoAdmin)
