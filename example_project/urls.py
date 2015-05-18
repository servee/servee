from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from servee import frontendadmin
frontendadmin.autodiscover()

urlpatterns = patterns("",
    (r"^admin/doc/", include("django.contrib.admindocs.urls")),
    (r"^admin/", include(admin.site.urls)),
    (r"^servee/", include(frontendadmin.site.urls)),

    (r"^login/$", "django.contrib.auth.views.login", {"template_name": "registration/login.html"}),
    (r"^logout/$", "django.contrib.auth.views.logout", {"template_name": "registration/logout.html", "next_page": "/"}),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r"^site_media/media/(?P<path>.*)$", "django.views.static.serve", {
            "document_root": settings.MEDIA_ROOT,
        }),
    )
