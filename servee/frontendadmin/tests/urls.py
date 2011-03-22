from django.conf.urls.defaults import *
import frontendadmin
import frontendadmin_registry


urlpatterns = patterns("",
    url(r"^servee/", include(frontendadmin.site.urls)),
)
