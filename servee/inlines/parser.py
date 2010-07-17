from django.template import TemplateSyntaxError
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.utils.encoding import smart_unicode
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
import ast
import datetime

def inlines(value, return_list=False):
    try:
        from BeautifulSoup import BeautifulStoneSoup
    except ImportError:
        from beautifulsoup import BeautifulStoneSoup

    content = BeautifulStoneSoup(value, selfClosingTags=['inline','img','br','input','meta','link','hr'])
    inline_list = []

    if return_list:
        for inline in content.findAll('inline'):
            rendered_inline = render_inline(inline)
            inline_list.append(rendered_inline['context'])
        return inline_list
    else:
        for inline in content.findAll('inline'):
            rendered_inline = render_inline(inline)
            if rendered_inline:
                inline.replaceWith(render_to_string(rendered_inline['template'], rendered_inline['context']))
            else:
                inline.replaceWith('')
        return mark_safe(content)


def render_inline(inline):
    """
    Replace inline markup with template markup that matches the
    appropriate app and model.

    """

    # Look for inline type, 'app.model'
    try:
        app_label, model_name = inline['type'].split('.')
    except:
        if settings.DEBUG:
            raise TemplateSyntaxError, "Couldn't find the attribute 'type' in the <inline> tag."
        else:
            return ''

    # Look for content type
    try:
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        model = content_type.model_class()
    except ContentType.DoesNotExist:
        if settings.DEBUG:
            raise TemplateSyntaxError, "Inline ContentType not found."
        else:
            return ''

    # Check for an inline class attribute
    try:
        inline_class = smart_unicode(inline['class'])
    except:
        inline_class = ''

    try:
        try:
            id_list = [int(i) for i in inline['ids'].split(',')]
            obj_list = model.objects.in_bulk(id_list)
            obj_list = list(obj_list[int(i)] for i in id_list)
            context = { 'object_list': obj_list, 'class': inline_class }
        except ValueError:
            if settings.DEBUG:
                raise ValueError, "The <inline> ids attribute is missing or invalid."
            else:
                return ''
    except KeyError:
        try:
            try:
                obj = model.objects.get(pk=inline['id'])
                context = { 'content_type':"%s.%s" % (app_label, model_name), 'object': obj, 'class': inline_class, 'settings': settings }
            except model.DoesNotExist:
                if settings.DEBUG:
                    raise model.DoesNotExist, "%s with pk of '%s' does not exist" % (model_name, inline['id'])
                else:
                    return ''
        except KeyError:
            try:
                l = inline['filter'].split(',')
                filterdict = dict()
                for item in l:
                    try:
                        item.index('=')
                        parts = item.split('=')
                        ## This should work for text, Need to test for all sorts of values
                        filterdict[parts[0]] = eval(parts[1])
                    except ValueError:
                        pass
                obj_list = list(model.objects.filter(**filterdict))
                context = { 'object_list': obj_list, 'class': inline_class }                
            except KeyError:
                if settings.DEBUG:
                    raise TemplateSyntaxError, "The <inline> filter attribute is missing or invalid."
                else:
                    return ''
            except ValueError:
                if settings.DEBUG:
                    raise TemplateSyntaxError, inline['filter'] + ' is bad, dummy.'
                else:
                    return ''
    
    # Set Default Template
    template = list()
    try:
        template.insert(0,inline['template'])
    except KeyError:
        pass
    template.extend(["inlines/%s_%s.html" % (app_label, model_name), "inlines/default.html"])
    
    rendered_inline = {'template':template, 'context':context}

    return rendered_inline