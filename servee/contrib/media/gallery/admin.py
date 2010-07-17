from django.contrib import admin
from servee.contrib.media.gallery.models import Gallery, GalleryItem,GalleryModel

class GalleryItemInline(admin.TabularInline):
    model = GalleryItem

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [GalleryItemInline,]
    
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryModel)
