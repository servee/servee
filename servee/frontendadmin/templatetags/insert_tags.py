"""
Some lame tags so that we can get urls.  This can be sorted out properly in 1.3, it's just not.
"""
from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template

register = template.Library()


class InsertRenderUrl(Tag):
    """
    Pass an insert and an object and get the insert.render_url(object)
    """
    name = "insert_render_url"
    
    options = Options(
        Argument('insert', required=True),
        Argument('obj', required=True)
    )
    
    def render_tag(self, context, insert, obj):
        return insert.render_url(obj)
    
register.tag(InsertRenderUrl)

class InsertDetailUrl(Tag):
    """
    Pass an insert and an object and get the insert.render_url(object)
    """
    name = "insert_detail_url"
    
    options = Options(
        Argument('insert', required=True),
        Argument('obj', required=True)
    )
    
    def render_tag(self, context, insert, obj):
        return insert.detail_url(obj)
    
register.tag(InsertDetailUrl)