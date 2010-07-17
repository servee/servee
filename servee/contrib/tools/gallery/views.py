from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
import datetime

from servee.contrib.media.gallery.models import Gallery, GalleryItem, GalleryModel

def add_to_gallery(request):
    """
    This view accepts 5 values (gallery, position, app_label, model, and pk) which are POSTed.
    Checks the values and adds the item at the specified position.
    """
    ret = {}
    ret['error'] = []
    
    # check fields
    fields = ['gallery','position','app_label','model','pk']
    for field in fields:
        if field not in request.POST.keys():
            ret['error'].append('Missing Field ' + field)
    if len(ret['error']):
       resp = simplejson.dumps(ret)
       return HttpResponse(resp)
       
    ## check permissions
    
    ## check that gallery and item exist
    gallery = Gallery.objects.get(pk=request.POST.get('gallery'))
    content_type = ContentType.objects.get(app_label = request.POST.get('app_label'), model=request.POST.get('model'))
    item = content_type.get_object_for_this_type(pk=request.POST.get('pk'))
    
    # add
    gallery_item = GalleryItem()
    gallery_item.content_type = content_type
    gallery_item.object_id = item.pk
    gallery_item.gallery = gallery
    gallery_item.order = request.POST.get('position')
    # save
    gallery_item.save()
    
    ret['item'] = 'success'
    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp)
    
def remove_from_gallery(request):
    """
    This view accepts two values (gallery, pk) which are POSTed.
    Checks the values and deletes the item at the specified gallery.
    """
    ret = {}
    ret['error'] = []
    
    # check fields
    fields = ['gallery','pk']
    for field in fields:
        if field not in request.POST.keys():
            ret['error'].append('Missing Field ' + field)
    if len(ret['error']):
       resp = simplejson.dumps(ret)
       return HttpResponse(resp)
    
    item = GalleryItem.objects.get(gallery=request.POST.get('gallery'), pk=request.POST.get('pk'))
    item.delete()

    ret['item'] = 'success'

    # return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp)
    
def create_gallery(request):
    """
    This view accepts no values and creates an empty Gallery with an auto-generated name.
    """
    ret = {}
    ret['error'] = []
    
    #auto name
    title = datetime.datetime.now().__str__()

    #create gallery
    gal = Gallery(title=title)
    gal.save()
    
    #build return
    ret['gallery'] = dict(title=title,pk=gal.pk)
    
    #return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp)
    
def update_gallery_order(request):
    """
    This view accepts a gallery, and a list of its items in order.
    """
    ret = {}
    ret['error'] = []
    
    # check fields
    fields = ['gallery','order']
    for field in fields:
        if field not in request.POST.keys():
            ret['error'].append('Missing Field ' + field)
    if len(ret['error']):
       resp = simplejson.dumps(ret)
       return HttpResponse(resp)
        
    #get gallery
    items = GalleryItem.objects.filter(gallery=request.POST.get('gallery'))
    order_s = request.POST.get('order').split(',')
    order = []
    for o in order_s:
        order.append(int(o))
    
    for item in items:
        new_order = order.index(item.pk)
        item.order = new_order
        item.save()
        
    #build return
    ret['item'] = 'success'

    #return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp)       
  
def change_gallery_title(request):
    """
    This view accepts a gallery, a title, and updates the title of the gallery.
    """  
    """
    This view accepts a gallery, and a list of its items in order.
    """
    ret = {}
    ret['error'] = []
    
    # check fields
    fields = ['gallery','title']
    for field in fields:
        if field not in request.POST.keys():
            ret['error'].append('Missing Field ' + field)
    if len(ret['error']):
       resp = simplejson.dumps(ret)
       return HttpResponse(resp)
       
    gal = Gallery.objects.get(pk=request.POST.get('gallery'))
    gal.title = request.POST.get('title')
    gal.save()
    
    #build return
    ret['item'] = 'success'

    #return result
    resp = simplejson.dumps(ret)
    return HttpResponse(resp)    
    