from django.contrib import admin
from sample_image_insert.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Image, ImageAdmin)
