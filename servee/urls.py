from django.conf.urls.defaults import *

urlpatterns = patterns("",
    # servee provided
    (r"^tools/gallery/", include('servee.contrib.tools.gallery.urls')),
    (r"^media/docs/", include('servee.contrib.media.document.urls')),
    (r"^media/images/", include('servee.contrib.media.image.urls')),
    (r"^media/video/", include('servee.contrib.media.video.urls')),
    (r"^atd/", include('servee.contrib.afterthedeadline.urls')),
)
