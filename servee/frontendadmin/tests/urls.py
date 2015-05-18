from django.conf.urls import patterns, url
import frontendadmin
import frontendadmin_registry


urlpatterns = patterns("",
    url(r"^servee/", include(frontendadmin.site.urls)),
)
