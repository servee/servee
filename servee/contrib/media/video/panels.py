from servee.wysiwyg.panels import InsertPanel
from django.template.loader import render_to_string
from servee.contrib.media.video.models import Video

class VideoPanel(InsertPanel):
    
    name = 'Video'
    has_content = True
    
    def nav_title(self):
        return 'Video'

    def title(self):
        return 'Video'
        
    def content(self):
        videos = Video.objects.all()
        return render_to_string('panels/video.html', dict(videos=videos))

    def url(self):
        return '#insert_video'