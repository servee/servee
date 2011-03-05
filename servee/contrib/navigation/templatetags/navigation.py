import copy

from django import template
from django.db.models import Q
from django.template import Node, NodeList, Variable
from servee.contrib.navigation.models import MenuItem

register = template.Library()

def menu_pages(menuitem):
    """ 
    Returns the childpages of <page> that <user> has access to.

    Usage: page|menu_pages:user

    For example:

    Homepage (online=True)
     \- PageA1 (menu=True, online=True)
          \- PageA2 (menu=True, online=True)
     \- PageB1 (inmenu=True, online=True)
          \- PageB2 (menu=True, online=True)

    When a request comes in for '/pageb1/pageb2/' the sitemanger
    passes the root of the site as `root` and the requested page as
    `page`. 

    A simple menu can be created like this:

    {% load navigation %}
    {% with page|currentmenu:2 as selectedmenu %}    
    <ul id="nav">
      <li><a href="/"{% if page.is_root %} class="current"{% endif %}>{{ page.get_root.title }}</a></li>
        {% for p in page.get_root|menu_pages:user %}<li>
        <a href="{{ p.get_absolute_url }}"{% ifequal p selectedmenu %}class="current"{% endifequal %}>{{ p.title }}</a>
      </li>
      {% endfor %}
    </ul>
    {% endwith %}

    There are a lot of variations on this theme in the various
    menu-types but most can be accomplished with similar incantations.

    """
    if not menuitem:
        menuitem = MenuItem.objects.get(urlpath='/')
    return menuitem.get_children().distinct()


def currentmenu(menuitem, depth):
    """
    Returns the (ancestral) page with inmenu=True and online=True
    at <depth>. Root is depth 1.

    You can use this to highlight 'current' items in a menu for
    example. See menu_pages for a demo.
    
    """
    if not menuitem:
        menuitem = MenuItem.objects.get(urlpath='/')
    if type(menuitem) != MenuItem:
        return None
    if menuitem.depth == depth:
        return menuitem
    menu = menuitem.get_ancestors().filter(depth=depth)
    if menu:
        return menu[0]


# This code is a (simplefied?) version of the same functionality in
# django-mptt for which we are eternally grateful
def tree_info(values):
    """
    Given a list of tree items, produces doubles of a tree item and a
    ``dict`` containing information about the tree structure around the
    item, with the following contents:
    
       new_level
          ``True`` if the current item is the start of a new level in
          the tree, ``False`` otherwise.

       closed_levels
          A list of levels which end after the current item. This will
          be an empty list if the next item is at the same level as the
          current item.

    Using this filter with unpacking in a ``{% for %}`` tag, you should
    have enough information about the tree structure to create a
    hierarchical representation of the tree.

    Example::

       {% for genre,structure in genres|tree_info %}
       {% if structure.new_level %}<ul><li>{% else %}</li><li>{% endif %}
       {{ genre.name }}
       {% for level in structure.closed_levels %}</li></ul>{% endfor %}
       {% endfor %}

    """
    structure = {}
    n = len(values)
    previous = None
    for i in range(n):
        # Get previous, current and next
        if i>0: previous = values[i-1]
        current = values[i]
        if i+1<n: 
            next = values[i+1]
        else:
            next = None

        if previous:
            structure['new_level'] = previous.depth < current.depth
        else:
            structure['new_level'] = True
        if next:
            structure['closed_levels'] = range(current.depth, next.depth, -1)
        else:
            structure['closed_levels'] = range(current.depth, 0, -1)
        yield current, copy.deepcopy(structure)

register.filter('menu_pages', menu_pages)
register.filter('currentmenu', currentmenu)
register.filter('tree_info', tree_info)

