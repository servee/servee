from django.forms.models import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
import datetime

from servee.contrib.media.image.forms import ImageUpload
from servee.contrib.media.image.models import Image

@csrf_exempt
def upload_image(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    ret = {}
    ret['error'] = []
    
    img = ImageUpload(request.POST, request.FILES)
    if img.is_valid():
        image = img.save()
        ret['item'] = render_to_string('panels/add_image.html',dict(image=image))
    else:
        ret['error'].append('Not a valid form')
        ret['error'].append(img.errors)
    
    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp, mimetype='text/plain')