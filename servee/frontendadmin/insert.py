from django.template.loader import get_template
from django.conf import settings

class BaseInsert(object):
    
    def _base_url(self):
        """
        Should not be overwritten
        """
        return self.__name__
    
    def nav_title(self):
        return self.__name__
    
    def title(self):
        return self.__name__
    
    def items(self):
        return NotImplementedError
    
    def get_items(self):
        return NotImplementedError
    
    def add_item(self):
        return NotImplementedError
    
    def edit_item(self, item):
        return NotImplementedError
    
    def content(self):
        return NotImplementedError

class ModelInsert(BaseInsert):
    """
    Should only be subclassed, never just _used_
    """
    ordering = None
    model = None
    
    
    def __init__(self, *args, **kwargs):
        """
        self.model should be set before calling super(<NewClass>, self).__init__...
        """
        self.item_display_template = [
            "servee/wysiwyg/insert/%s/%s/_list.html" % (self.model.app_label, self.model.module_name),
            "servee/wysiwyg/insert/%s/_list.html" % (self.model.app_label),            
            "servee/wysiwyg/insert/_item_list.html",
            ]
        self.item_detail_template = [
            "servee/wysiwyg/insert/%s/%s/_detail.html" % (self.model.app_label, self.model.module_name),
            "servee/wysiwyg/insert/%s/_detail.html" % (self.model.app_label),            
            "servee/wysiwyg/insert/_item_detail.html",
            ]
        self.item_render_template  = [
            "servee/wysiwyg/insert/%s/%s/_render.html" % (self.model.app_label, self.model.module_name),
            "servee/wysiwyg/insert/%s/_render.html" % (self.model.app_label),            
            "servee/wysiwyg/insert/_item_render.html",
            ]
        super(ModelInsert, self).__init__(*args, **kwargs)
    
    
    def queryset(self, ordering=None):
        qs = self.model._default_manager.get_query_set()
        if not ordering:
            ordering = self.ordering or () # otherwise we might try to *None, which is bad ;)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
    
    
    def items(self):
        return self.queryset()
    
    
    def render(self, item):
        """
        Gets an item pk, and renders it to HTML string to be insert.
        item is passed to the template (item_render_template) with context
        item,
        MEDIA_URL,
        STATIC_URL
        """
        item = self.model._default_manager.get(pk=item)
        t = get_template(self.item_render_template)
        return t.render({
                            "MEDIA_URL": settings.MEDIA_URL,
                            "STATIC_URL": settings.STATIC_URL,
                            "item": item,
                        })
    
    
    def get_items(self):
        """
        Ideally, this will be a method that will also take a request, for pagination, or filtering
        """
        return self.items()
