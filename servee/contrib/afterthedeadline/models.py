from django.conf.urls.defaults import *

urlpatterns = patterns('servee.contrib.afterthedeadline.views',
    url(r'^afterthedeadline/$', view='afterthedeadline', name='afterthedeadline'),
)