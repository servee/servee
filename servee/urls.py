from django.conf.urls.defaults import url, patterns, include
from django.conf import settings

urlpatterns = patterns("",
    url(r"^nop/", "NOP")
)

if "servee.contrib.media.document" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        url(r"^media/docs/", include("servee.contrib.media.document.urls")),
    )

if "servee.contrib.tools.gallery" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        url(r"^tools/gallery/", include("servee.contrib.tools.gallery.urls")),
    )

if "servee.contrib.media.image" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        url(r"^media/images/", include("servee.contrib.media.image.urls")),
    )
    
if "servee.contrib.media.video" in settings.INSTALLED_APPS:
    urlpatterns += patterns("",
        (r"^media/video/", include("servee.contrib.media.video.urls")),
    )
