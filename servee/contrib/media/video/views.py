from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from servee.contrib.media.video.forms import VideoUpload

@csrf_exempt
def upload_video(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    vid = VideoUpload(request.POST, request.FILES)
    if vid.is_valid():
        video = vid.save()
        return render_to_response('panels/add_video.html',dict(video=video))
    else:
        return HttpResponse(vid.errors[0]);