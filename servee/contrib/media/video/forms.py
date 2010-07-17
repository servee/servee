from django import forms
from servee.contrib.media.video.models import Video

class VideoUpload(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video',)