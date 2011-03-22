from servee import frontendadmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatpageForm
from django.utils.translation import ugettext_lazy as _

class FlatPageFrontendadminAdmin(frontendadmin.ServeeModelAdmin):
    """
    This class extends from the normal FlatPageAdmin, as well as frontendadmin.ServeeModelAdmin
    The later simply adds to the templates that should be processed when looking
    for the templates to render this page.
    """
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

frontendadmin.site.register(FlatPage, FlatPageFrontendadminAdmin)