from django.contrib.admin.sites import AdminSite

class ServeeAdminSite(AdminSite):
    """
    Like AdminSite, but the registered ModelAdmin classes are expected to be used
    by frontend administrators, content editors, etc.
    """
    
    insert_classes = []
    toolbar_classes = []
    
    def register_insert(self, class_registered):
        """
        ...
        """
        self.insert_classes.append(class_registered)
    
    def register_toolbar(self, class_registered):
        """
        ...
        """
        self.toolbar_classes.append(class_registered)
    
    def __init__(self, *args, **kwargs):
        super(ServeeAdminSite, self).__init__(*args, **kwargs)
        self.name = "servee"
        self.app_name = "servee"
        
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