from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

import frontendadmin

class FlatPageFrontendadminAdmin(FlatPageAdmin, frontendadmin.ServeeModelAdmin):
    """
    This class extends from the normal FlatPageAdmin, as well as frontendadmin.ServeeModelAdmin
    The later simply adds to the templates that should be processed when looking
    for the templates to render this page.
    """
    pass

frontendadmin.site.register(FlatPage, FlatPageFrontendadminAdmin)
