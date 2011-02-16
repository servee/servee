from django.conf import settings
from django.template.loader import render_to_string
from servee.wysiwyg.panels import InsertPanel
from servee.contrib.media.video.models import Video
from servee.contrib.media.video.forms import VideoUpload

class VideoPanel(InsertPanel):
    
    name = 'Video'
    has_content = True
    
    def nav_title(self):
        return 'Video'

    def title(self):
        return 'Video'
        
    def content(self):
        videos = Video.objects.all()
        form = VideoUpload()
        return render_to_string('panels/video.html', dict(videos=videos, form=form, STATIC_URL=settings.STATIC_URL))

    def url(self):
        return '#insert_video'