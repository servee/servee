from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from django.core.urlresolvers import reverse
from django.db.models import Model
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


register = template.Library()

class AddObject(Tag):
    name = "frontendadmin_add"

    options = Options(
        Argument('queryset_instance', required=True),
        Argument('label', required=False, resolve=False)
    )

    def render_tag(self, context, model_instance, label=None):
        if not isinstance(queryset_instance, QuerySet):
            raise template.TemplateSyntaxError, "'%s' argument must be a queryset" % queryset_instance

        user = context["request"].user
        if not user:
            return ""

        app_label = queryset_instance.model._meta.app_label
        model_name = queryset_instance.model._meta.module_name

        if not user.has_perm("%s.add" % app_label):
            return ""

        if not label:
            label = _("Add")

        return '<a class="frontendadmin frontendadmin_add" href="%s">%s</a>' % (
            reverse("servee:%s_%s_add" % (
                    app_label,
                    model_name,
                ), args=[model_instance.pk,]
            ),
            label
        )

class ChangeObject(Tag):
    name = "frontendadmin_change"

    options = Options(
        Argument('model_instance', required=True),
        Argument('label', required=False, resolve=False)
    )

    def render_tag(self, context, model_instance, label=None):
        if not isinstance(model_instance, Model):
            raise template.TemplateSyntaxError, "'%s' argument must be a model-instance" % model_instance

        user = context["request"].user
        if not user:
            return ""

        app_label = model_instance._meta.app_label
        model_name = model_instance._meta.module_name

        if not user.has_perm("%s.change" % app_label, model_instance):
            return ""

        if not label:
            label = _("Change")

        return '<a class="frontendadmin frontendadmin_edit" href="%s">%s</a>' % (
            reverse("servee:%s_%s_change" % (
                    app_label,
                    model_name,
                ), args=[model_instance.pk,]
            ),
            label
        )

class DeleteObject(Tag):
    name = "frontendadmin_delete"

    options = Options(
        Argument('model_instance', required=True),
        Argument('label', required=False, resolve=False)
    )

    def render_tag(self, context, model_instance, label=None):
        if not isinstance(model_instance, Model):
            raise template.TemplateSyntaxError, "'%s' argument must be a model-instance" % model_instance

        user = context["request"].user
        if not user:
            return ""

        app_label = model_instance._meta.app_label
        model_name = model_instance._meta.module_name

        if not user.has_perm("%s.delete" % app_label, model_instance):
            return ""

        if not label:
            label = _("Delete")

        return '<a class="frontendadmin frontendadmin_delete" href="%s">%s</a>' % (
            reverse("servee:%s_%s_delete" % (
                    app_label,
                    model_name,
                ), args=[model_instance.pk,]
            ),
            label
        )

register.tag(AddObject)
register.tag(ChangeObject)
register.tag(DeleteObject)