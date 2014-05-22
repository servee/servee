from django import template

register = template.Library()

def submit_row_frontendadmin(context):
    """
    Displays the row of buttons for delete and save.
    """
    opts = context['opts']
    change = context['change']
    is_popup = context['is_popup']
    save_as = context['save_as']
    return {
        #'show_delete_link': (not is_popup and context['has_delete_permission']
        #                      and (change or context['show_delete'])),
        'show_save_as_new': not is_popup and change and save_as,
        'show_save_and_add_another': context['has_add_permission'] and
                            not is_popup and (not save_as or context['add']),
        'show_save_and_continue': not is_popup and context['has_change_permission'],
        'is_popup': is_popup,
        'show_save': True
    }
register.inclusion_tag('servee/_submit_line.html', takes_context=True)(submit_row_frontendadmin)
