from django.contrib.admin.sites import AdminSite, AlreadyRegistered
from django.conf import settings

class ServeeAdminSite(AdminSite):
    """
    Like AdminSite, but the registered ModelAdmin classes are expected to be used
    by frontend administrators, content editors, etc.
    """
    
    insert_classes = {}
    custom_views = []
    
    def register_view(self, path, view, name=None):
        """
        Lifted from AdminPlus: https://github.com/jsocol/django-adminplus/blob/master/adminplus/__init__.py
        Add a custom admin view.

        * `path` is the path in the admin where the view will live, e.g.
            http://example.com/admin/somepath
        * `view` is any view function you can imagine.
        * `name` is an optional pretty name for the list of custom views. If
            empty, we'll guess based on view.__class__.__name__.
        """
        self.custom_views.append((path, view, name))
    
    def register_insert(self, class_registered):
        """
        ...
        """
        insert_class = class_registered(self)
        
        if self.insert_classes.get(insert_class.base_url()):
            raise AlreadyRegistered("An insert with the base_url (lowercase classname) of %s is already registered" % insert_class.base_url)
        
        # Add to registry of instantiated models
        self.insert_classes[insert_class.base_url()] = insert_class
    
    def unregister_insert(self, class_registered):
        """
        Removes a class from the insert_classes dictionary.  This is useful if a
        third party registerd the class, and you want to edit it.
        """
        insert_class = class_registered(self)
        
        if self.insert_classes.get(insert_class.base_url()):
            self.insert_classes.pop(insert_class.base_url())
        
    
    def get_urls(self):
        """Add our custom views to the admin urlconf."""
        urls = super(ServeeAdminSite, self).get_urls()
        from django.conf.urls.defaults import patterns, url, include
        
        # Custom Views
        for path, view, name in self.custom_views:
            urls += patterns('',
                url(r'^%s$' % path, self.admin_view(view)),
            )
        
        # Inserts
        for insert_model_lookup, insert in self.insert_classes.iteritems():
            urls += patterns("",
                (r"^insert/%s/%s/" % (insert.model._meta.app_label, insert.model._meta.module_name), include(insert.urls))
            )
        return urls
    
    def __init__(self, *args, **kwargs):
        super(ServeeAdminSite, self).__init__(*args, **kwargs)
        
        ##@@ TODO Fix so that this can be properly namespaced
        self.name = "servee"
        self.app_name = "servee"
        self.uses_wysiwyg = "servee.wysiwyg" in settings.INSTALLED_APPS
        
        self.index_template = ["servee/index.html", "admin/index.html"]
        self.login_template = ["servee/login.html", "admin/login.html"]
        self.logout_template = ["servee/logout.html", "admin/logout.html"]
        self.password_change_template = ["servee/password_change.html", "admin/password_change.html"]
        self.password_change_done_template = ["servee/password_change_done.html", "admin/password_change_done.html"]

    def app_index(self, request, app_label, extra_context=None):
        self.app_index_template = (
            "servee/%s/app_index.html" % app_label,
            "servee/app_index.html",
            "admin/%s/app_index.html" % app_label,
            "admin/app_index.html",
        )
        super(ServeeAdminSite, self).app_index(request, app_label, extra_context)

site = ServeeAdminSite()