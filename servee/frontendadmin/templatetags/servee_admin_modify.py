from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
register = template.Library()

submit_row = register.inclusion_tag('servee/_submit_line.html', takes_context=True)(submit_row)