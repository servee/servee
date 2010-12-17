from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from servee.contrib.media.image.forms import DocumentUpload

@csrf_exempt
def upload_image(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    doc = DocumentUpload(request.POST, request.FILES)
    if doc.is_valid():
        document = doc.save()
        return render_to_response('panels/add_document.html',dict(document=document))
    else:
        return HttpResponse(doc.errors[0]);