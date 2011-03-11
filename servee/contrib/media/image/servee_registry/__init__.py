from servee import frontendadmin
from servee.contrib.media.image.servee_registry.insert import ImageInsert

frontendadmin.site.register_insert(ImageInsert)