from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from servee.contrib.media.video.forms import VideoUpload


@csrf_exempt
def upload_video(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    ret = {}
    ret['error'] = []
    
    vid = VideoUpload(request.POST, request.FILES)
    if vid.is_valid():
        video = vid.save()
        ret['item'] = render_to_string('panels/add_video.html',dict(video=video))
    else:
        ret['error'].append('Not a valid form')
        ret['error'].append(vid.errors)
    
    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp, mimetype='application/json')