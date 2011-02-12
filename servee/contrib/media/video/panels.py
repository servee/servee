from servee.wysiwyg.panels import InsertPanel
from django.template.loader import render_to_string
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
        return render_to_string('panels/video.html', dict(videos=videos, form=form))

    def url(self):
        return '#insert_video'