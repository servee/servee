from servee.toolbar.panels import ToolPanel
from django.template.loader import render_to_string
from servee.contrib.media.gallery.models import Gallery, GalleryModel

class BuildGalleryPanel(ToolPanel):
    
    name = 'Galleries'
    has_content = True
    
    def nav_title(self):
        return 'Galleries'

    def title(self):
        return 'Galleries'
        
    def content(self):
        galleries = Gallery.objects.all()
        models = GalleryModel.objects.all()
        
        types = []
        for model in models:
            temp = {}
            temp['instance'] = model.content_type.model_class()
            temp['name'] = model.content_type.name.lower()
            temp['app_label'] = model.content_type.app_label
            temp['model'] = model.content_type.model
            types.append(temp)
            
        context = self.context.copy()
        context.update(dict(galleries=galleries,types=types)) 
        
        return render_to_string('toolbar/gallery.html', context)

    def url(self):
        return '#edit_gallery'