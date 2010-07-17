"""
The main DebugToolbar class that loads and renders the Toolbar.
"""
from django.conf import settings
from django.template.loader import render_to_string

class Wysiwyg(object):

    def __init__(self, request):
        self.request = request
        self.panels = []
        base_url = self.request.META.get('SCRIPT_NAME', '')
        self.config = {}
        
        # Check if settings has a WYSIWYG_CONFIG and updated config
        self.config.update(getattr(settings, 'WYSIWYG_CONFIG', {}))
        self.template_context = {
            'BASE_URL': base_url, # for backwards compatibility
        }
        # Override this tuple by copying to settings.py as `WYSIWYG_INSERT_MODELS`
        self.default_panels = (
            'servee.contrib.media.image.panels.ImagePanel',
            'servee.contrib.media.video.panels.VideoPanel',
            'servee.contrib.media.document.panels.DocumentPanel',
            'servee.contrib.media.gallery.panels.GalleryPanel',
        )
        self.load_panels()

    def load_panels(self):
        """
        Populate insert panels
        """
        from django.core import exceptions

        # Check if settings has a WYSIWYG_INSERT_MODELS, otherwise use default
        if hasattr(settings, 'WYSIWYG_INSERT_MODELS'):
            self.default_panels = settings.WYSIWYG_INSERT_MODELS

        for panel_path in self.default_panels:
            try:
                dot = panel_path.rindex('.')
            except ValueError:
                raise exceptions.ImproperlyConfigured, '%s isn\'t a wysiwyg insert panel module' % panel_path
            panel_module, panel_classname = panel_path[:dot], panel_path[dot+1:]
            try:
                mod = __import__(panel_module, {}, {}, [''])
            except ImportError, e:
                raise exceptions.ImproperlyConfigured, 'Error importing wysiwyg insert panel %s: "%s"' % (panel_module, e)
            try:
                panel_class = getattr(mod, panel_classname)
            except AttributeError:
                raise exceptions.ImproperlyConfigured, 'Wysiwyg Insert Panel module "%s" does not define a "%s" class' % (panel_module, panel_classname)

            try:
                context = self.template_context.copy()
                context.update({'STATIC_URL': settings.STATIC_URL, 'DEBUG': settings.DEBUG })
                panel_instance = panel_class(context=context)
            except:
                raise # Bubble up problem loading panel

            self.panels.append(panel_instance)

    def render_toolbar(self):
        """
        Renders the overall Toolbar with panels inside.
        """
        if hasattr(settings, 'SRV_WYSIWYG_EDITOR'):
            SRV_WYSIWYG_EDITOR = settings.SRV_WYSIWYG_EDITOR
        else: 
            SRV_WYSIWYG_EDITOR = 'tinymce'
        context = self.template_context.copy()
        context.update({ 'panels': self.panels, 'STATIC_URL': settings.STATIC_URL, 'DEBUG': settings.DEBUG })

        ui = render_to_string('wysiwyg/tools.html', context)
        js = render_to_string('wysiwyg/js_'+SRV_WYSIWYG_EDITOR+'.html',context)
        return ui+js
