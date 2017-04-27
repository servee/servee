from django.conf.urls import url
import frontendadmin
import frontendadmin_registry


urlpatterns = [
    url(r"^servee/", include(frontendadmin.site.urls)),
]
