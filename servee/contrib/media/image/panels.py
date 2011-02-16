from django.conf import settings
from django.template.loader import render_to_string
from servee.wysiwyg.panels import InsertPanel
from servee.contrib.media.image.forms import ImageUpload
from servee.contrib.media.image.models import Image

class ImagePanel(InsertPanel):
    
    name = 'Image'
    has_content = True
    
    def nav_title(self):
        return 'Image'

    def title(self):
        return 'Image'
        
    def content(self):
        images = Image.objects.all()
        form = ImageUpload()
        
        context = self.context.copy()
        context.update(dict(images=images, form=form, STATIC_URL=settings.STATIC_URL))
        
        return render_to_string('panels/image.html', context)

    def url(self):
        return '#insert_image'