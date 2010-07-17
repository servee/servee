from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from servee.contrib.afterthedeadline import atd


@csrf_exempt
def proxy(request):
    key = settings.ATD_KEY
    atd.setDefaultKey(key)
    if(request.GET.get('url') == '/checkDocument'):
        HttpResponse(atd.checkDocument(request.POST.get('data')))
    else:
        HttpResponse(atd.stats(request.POST.get('data')))