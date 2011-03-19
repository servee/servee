from servee import frontendadmin
from servee.frontendadmin.insert import ModelInsert
from sample_insert.image.models import Image

class ImageInsert(ModelInsert):
    model = Image

frontendadmin.site.register_insert(ImageInsert)