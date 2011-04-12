from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


register = template.Library()

def check_permission(user, action_name, app_label, model_name):
    """
    Check for proper permissions. action_name may be either add, change or delete.
    """
    p = '%s.%s_%s' % (app_label, action_name, model_name)
    return user and user.is_active and user.has_perm(p)

class AddObject(Tag):
    name = "frontendadmin_add"

    options = Options(
        Argument('querysetish', required=True),
        Argument('label', required=False, resolve=False),
        Argument('add_class', required=False, resolve=False)
    )

    def render_tag(self, context, querysetish, label=None, add_class=None):
        if isinstance(querysetish, basestring):
            app_label, model_name = querysetish.lower().split(".")
            content_type = ContentType.objects.get(app_label=app_label, model=model_name)
            model = content_type.model_class()
            queryset_instance = model._default_manager.get_query_set()
        elif isinstance(querysetish, QuerySet):
            queryset_instance = querysetish
        else:
            raise template.TemplateSyntaxError, "'%s' argument must be a queryset or string representation" % queryset_instance

        user = context["request"].user
        app_label = queryset_instance.model._meta.app_label
        model_name = queryset_instance.model._meta.module_name

        if not check_permission(user, "add", app_label, model_name):
            return ""

        if not label:
            label = _("Add")

        return '<a class="frontendadmin frontendadmin_add %s" href="%s">%s</a>' % (
            add_class,
            reverse("servee:%s_%s_add" % (app_label, model_name,)),
            unicode(label)
        )

class ChangeObject(Tag):
    name = "frontendadmin_change"

    options = Options(
        Argument('model_instance', required=True),
        Argument('label', required=False, resolve=False),
        Argument('add_class', required=False, resolve=False)
    )

    def render_tag(self, context, model_instance, label=None, add_class=None):
        if not isinstance(model_instance, Model):
            raise template.TemplateSyntaxError, "'%s' argument must be a model-instance" % model_instance

        user = context["request"].user
        app_label = model_instance._meta.app_label
        model_name = model_instance._meta.module_name

        if not check_permission(user, "change", app_label, model_name):
            return ""

        if not label:
            label = _("Change")

        return '<a class="frontendadmin frontendadmin_edit %s" href="%s">%s</a>' % (
            add_class,
            reverse("servee:%s_%s_change" % (
                    app_label,
                    model_name,
                ), args=[model_instance.pk,]
            ),
            unicode(label)
        )


class ListObjects(Tag):
    """
    ListObjects is by far the weakest tag/area of servee.  No tests, no permalinks,
    
    If you must use it, write documentation, help me solidify the API.
    """
    
    name = "frontendadmin_list"

    options = Options(
        Argument('modelish', required=True),
        Argument('label', required=False, resolve=False),
        Argument('add_class', required=False, resolve=False)
    )

    def render_tag(self, context, modelish, label=None, add_class=None):
        if isinstance(modelish, basestring):
            app_label, model_name = modelish.lower().split(".")
            content_type = ContentType.objects.get(app_label=app_label, model=model_name)
            model = content_type.model_class()
        elif isinstance(modelish, QuerySet):
            model = modelish.model
        elif isinstance(modelish, Model):
            model = modelish
        else:
            raise template.TemplateSyntaxError, "'%s' argument must be a model-instance, queryset, or string representation" % modelish

        user = context["request"].user
        app_label = model._meta.app_label
        model_name = model._meta.module_name

        if not check_permission(user, "change", app_label, model_name):
            return ""

        if not label:
            label = _("List")

        return '<a class="frontendadmin frontendadmin_list %s" href="%s">%s</a>' % (
            add_class,
            reverse("servee:%s_%s_changelist" % (
                    app_label,
                    model_name,
                )
            ),
            unicode(label)
        )


class DeleteObject(Tag):
    name = "frontendadmin_delete"

    options = Options(
        Argument('model_instance', required=True),
        Argument('label', required=False, resolve=False),
        Argument('add_class', required=False, resolve=False)
    )

    def render_tag(self, context, model_instance, label=None, add_class=None):
        if not isinstance(model_instance, Model):
            raise template.TemplateSyntaxError, "'%s' argument must be a model-instance" % model_instance

        user = context["request"].user
        app_label = model_instance._meta.app_label
        model_name = model_instance._meta.module_name

        if not check_permission(user, "delete", app_label, model_name):
            return ""

        if not label:
            label = _("Delete")

        return '<a class="frontendadmin frontendadmin_delete %s" href="%s">%s</a>' % (
            add_class,
            reverse("servee:%s_%s_delete" % (
                    app_label,
                    model_name,
                ), args=[model_instance.pk,]
            ),
            unicode(label)
        )

register.tag(AddObject)
register.tag(ChangeObject)
register.tag(DeleteObject)
register.tag(ListObjects)