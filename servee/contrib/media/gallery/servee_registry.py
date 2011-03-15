from servee import frontendadmin
from servee.contrib.media.gallery.models import Gallery

class GalleryInsert(frontendadmin.ModelInsert):
    model = Gallery


frontendadmin.site.register_insert(GalleryInsert)