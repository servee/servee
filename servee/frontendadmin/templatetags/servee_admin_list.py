from django import template
register = template.Library()

def search_form_servee(context, cl):
    """
    Yet another thing I had to subclass strictly so
    I could put a proper full-url into a form action or a link
    """
    return {
        "request": context["request"],
        "cl": cl,
        "show_result_count": cl.result_count != cl.full_result_count,
        "search_var": "q"
    }
search_form_servee = register.inclusion_tag("servee/_search_form.html", takes_context=True)(search_form_servee)