from servee.wysiwyg.panels import InsertPanel
from django.template.loader import render_to_string
from servee.contrib.media.gallery.models import Gallery

class GalleryPanel(InsertPanel):
    
    name = 'Gallery'
    has_content = True
    
    def nav_title(self):
        return 'Gallery'

    def title(self):
        return 'Gallery'
        
    def content(self):
        galleries = Gallery.objects.all()
        return render_to_string('panels/gallery.html', dict(galleries=galleries))

    def url(self):
        return '#insert_gallery'