from django.conf.urls.defaults import *

urlpatterns = patterns('servee.contrib.tools.gallery.views',
    url(r'^add_to_gallery/$', view='add_to_gallery', name='add_to_gallery'),
    url(r'^remove_from_gallery/$', view='remove_from_gallery', name='remove_from_gallery'),
    url(r'^create_gallery/$', view='create_gallery', name='create_gallery'),
    url(r'^update_gallery_order/$', view='update_gallery_order', name='update_gallery_order'),
    url(r'^change_gallery_title/$', view='change_gallery_title', name='change_gallery_title'),
)