from django.conf.urls.defaults import *

urlpatterns = patterns('servee.contrib.media.video.views',
    url(r'^upload_video/$', view='upload_video', name='upload_video'),
)