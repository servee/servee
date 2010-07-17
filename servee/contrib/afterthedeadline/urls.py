from django.conf.urls.defaults import *

urlpatterns = patterns('servee.contrib.afterthedeadline.views',
    url(r'^proxy/$', view='proxy', name='afterthedeadline_proxy'),
)