# ACTION_CHECKBOX_NAME is unused, but should stay since its import from here
# has been referenced in documentation.
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin.options import HORIZONTAL, VERTICAL
from servee.frontendadmin.options import ServeeModelAdmin
from servee.frontendadmin.options import StackedInline, TabularInline
from servee.frontendadmin.sites import ServeeAdminSite, site
from servee.frontendadmin.insert import ModelInsert

def autodiscover():
    """
    Auto-discover INSTALLED_APPS servee.py modules and fail silently when
    not present. This forces an import on them to register any admin bits they
    may want.
    """

    import copy
    from django.conf import settings
    from importlib import import_module
    from django.utils.module_loading import module_has_submodule

    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        # Attempt to import the app's admin module.
        try:
            before_import_registry = copy.copy(site._registry)
            import_module('%s.servee_registry' % app)
        except:
            # Reset the model registry to the state before the last import as
            # this import will have to reoccur on the next request and this
            # could raise NotRegistered and AlreadyRegistered exceptions
            # (see #8245).
            site._registry = before_import_registry

            # Decide whether to bubble up this error. If the app just
            # doesn't have an admin module, we can ignore the error
            # attempting to import it, otherwise we want it to bubble up.
            if module_has_submodule(mod, 'servee_registry'):
                raise
