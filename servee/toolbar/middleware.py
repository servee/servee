"""
Debug Toolbar middleware
"""
import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.encoding import smart_unicode
from django.conf.urls.defaults import include, patterns
from django.core.urlresolvers import reverse

import servee.toolbar.urls
from servee.toolbar.loader import Toolbar

_HTML_TYPES = ('text/html', 'application/xhtml+xml')

def replace_insensitive(string, target, replacement):
    """
    Similar to string.replace() but is case insensitive
    Code borrowed from: http://forums.devshed.com/python-programming-11/case-insensitive-string-replace-490921.html
    """
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else: # no results so return the original string
        return string

class ToolbarMiddleware(object):
    """
    Middleware to set up Toolbar on incoming request and render toolbar
    on outgoing response.
    """
    def __init__(self):
        self.toolbar = {}

        # Set method to use to decide to show toolbar
        self.show_toolbar = self._show_toolbar # default

        # The tag to attach the toolbar to
        self.tag= u'</body>'

        self.show_in_admin = False

        if hasattr(settings, 'TOOLBAR_CONFIG'):
            show_toolbar_callback = settings.TOOLBAR_CONFIG.get(
                'SHOW_TOOLBAR_CALLBACK', None)
            if show_toolbar_callback:
                self.show_toolbar = show_toolbar_callback

            tag = settings.TOOLBAR_CONFIG.get('TAG', None)
            if tag:
                self.tag = u'</' + tag + u'>'
        
            show_in_admin = settings.WYSIWYG_CONFIG.get('SHOW_IN_ADMIN', None)
            if show_in_admin:
                self.show_in_admin = show_in_admin

    def _show_toolbar(self, request):
        if (request.is_ajax() \
          or not request.user \
          or not request.user.is_staff) \
          or (not self.show_in_admin and request.path.startswith(reverse('admin:index'))):
            return False
        return True

    def process_request(self, request):
        if self.show_toolbar(request):
            #request.urlconf = 'debug_toolbar.urls'
            self.toolbar[request] = Toolbar(request)
            for panel in self.toolbar[request].panels:
                panel.process_request(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request in self.toolbar:
            for panel in self.toolbar[request].panels:
                panel.process_view(request, view_func, view_args, view_kwargs)

    def process_response(self, request, response):
        if response.status_code == 200 \
          and self.show_toolbar(request):
            for panel in self.toolbar[request].panels:
                panel.process_response(request, response)
            if response['Content-Type'].split(';')[0] in _HTML_TYPES:
                response.content = replace_insensitive(
                    smart_unicode(response.content), 
                    self.tag,
                    smart_unicode(self.toolbar[request].render_toolbar() + self.tag))
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)
        #del self.wysiwyg[request].panels
        return response