from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from servee.contrib.media.image.forms import ImageUpload

@csrf_exempt
def upload_image(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    img = ImageUpload(request.POST, request.FILES)
    if img.is_valid():
        image = img.save()
        return render_to_response('panels/add_image.html',dict(image=image))
    else:
        return HttpResponse(img.errors[0]);