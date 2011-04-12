from django.contrib.admin.options import ModelAdmin, StackedInline, TabularInline
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin.util import quote
from django.http import HttpResponse, HttpResponseRedirect

class ServeeChangeList(ChangeList):
    """
    I need full path links everywhere in the admin,
    so I subclassed the changelist.  This makes me a sad
    panda.
    """
    
    def url_for_result(self, result):    
        return "/servee/%s/%s/%s/" % (
            self.model._meta.app_label,
            self.model._meta.object_name.lower(),
            quote(getattr(result, self.pk_attname)),
        )


class ServeeModelAdmin(ModelAdmin):
    """
    ServeeModelAdmin is just like the normal ModelAdmin, but with a larger pool of default
    templates.  First it uses the template specifically registered with the ModelAdmin (normal behavior)
    the difference is the fallback, where normally it would check admin/...  it first checks servee/...
    """
        
    def __init__(self, *args, **kwargs):
        super(ServeeModelAdmin, self).__init__(*args, **kwargs)
        opts = self.model._meta
        app_label = opts.app_label
        
        self.change_form_template =  [
            "servee/%s/%s/change_form.html" % (app_label, opts.object_name.lower()),
            "servee/%s/change_form.html" % app_label,
            "servee/change_form.html",
            "admin/%s/%s/change_form.html" % (app_label, opts.object_name.lower()),
            "admin/%s/change_form.html" % app_label,
            "admin/change_form.html",
        ]
        self.add_form_template =  [
            "servee/%s/%s/add_form.html" % (app_label, opts.object_name.lower()),
            "servee/%s/add_form.html" % app_label,
            "admin/%s/%s/add_form.html" % (app_label, opts.object_name.lower()),
            "admin/%s/add_form.html" % app_label,
        ].append(self.change_form_template)
        self.change_list_template =  [
            "servee/%s/%s/change_list.html" % (app_label, opts.object_name.lower()),
            "servee/%s/change_list.html" % app_label,
            "servee/change_list.html",
            "admin/%s/%s/change_list.html" % (app_label, opts.object_name.lower()),
            "admin/%s/change_list.html" % app_label,
            "admin/change_list.html",
        ]
        self.delete_confirmation_template = [
            "servee/%s/%s/delete_confirmation.html" % (app_label, opts.object_name.lower()),
            "servee/%s/delete_confirmation.html" % app_label,
            "servee/delete_confirmation.html",
            "admin/%s/%s/delete_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_confirmation.html" % app_label,
            "admin/delete_confirmation.html",
        ]
        self.delete_selected_confirmation_template = [
            "servee/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "servee/%s/delete_selected_confirmation.html" % app_label,
            "servee/delete_selected_confirmation.html",
            "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
            "admin/%s/delete_selected_confirmation.html" % app_label,
            "admin/delete_selected_confirmation.html",
        ]
        self.object_history_template = [
            "servee/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "servee/%s/object_history.html" % app_label,
            "servee/object_history.html",
            "admin/%s/%s/object_history.html" % (app_label, opts.object_name.lower()),
            "admin/%s/object_history.html" % app_label,
            "admin/object_history.html",
        ]
    

    def response_add(self, request, obj):
        """
        Act differently during frontendadmin(ajax) just reload the page.
        """

        # in these cases, the redirect is good
        if list(set(request.POST.keys()) & set(["_addanother", "_continue"])):
            return super(ServeeModelAdmin, self).response_change(request, obj)

        # we want to override the default save case in the frontend
        ref = request.META.get("HTTP_REFERER")
        if ref and (ref.find("/servee/") == -1):
            if request.is_ajax():
                return HttpResponse("<script type='text/javascript'>window.location.reload(true);</script>")
            else:
                return HttpResponseRedirect(ref)

        # fallback to normal functionality
        return super(ServeeModelAdmin, self).response_add(request, obj)


    def response_change(self, request, obj):
        """
        Act differently during frontendadmin(ajax) just reload the page.
        """
        
        # in these cases, the redirect is good
        if list(set(request.POST.keys()) & set(["_addanother", "_saveasnew", "_continue"])):
            return super(ServeeModelAdmin, self).response_change(request, obj)
        
        # we want to override the default save case in the frontend
        ref = request.META.get("HTTP_REFERER")
        if ref and (ref.find("/servee/") == -1):
            if request.is_ajax():
                return HttpResponse("<script type='text/javascript'>window.location.reload(true);</script>")
            else:
                return HttpResponseRedirect(ref)
        
        # fallback to normal functionality
        return super(ServeeModelAdmin, self).response_change(request, obj)
    
    def change_view(self, *args, **kwargs):
        """
        Add the insert_classes to the template context.
        """
        if not kwargs.get("extra_context"):
            kwargs["extra_context"] = {}
        kwargs["extra_context"].update({
            "insert_classes": self.admin_site.insert_classes,
        })
        return super(ServeeModelAdmin, self).change_view(*args, **kwargs)
    
    def add_view(self, *args, **kwargs):
        """
        Add the insert_classes to the template context.
        """
        if not kwargs.get("extra_context"):
            kwargs["extra_context"] = {}
        kwargs["extra_context"].update({
            "insert_classes": self.admin_site.insert_classes,
            "form_url": "herp"
        })
        return super(ServeeModelAdmin, self).add_view(*args, **kwargs)

    def get_changelist(self, request, **kwargs):
        return ServeeChangeList


class ServeeStackedInline(StackedInline):
    template = 'servee/edit_inline/stacked.html'

class ServeeTabularInline(TabularInline):
    template = 'servee/edit_inline/tabular.html'
