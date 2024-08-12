from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    def build_menu(items, parent=None):
        menu = []
        for item in items:
            children = items.filter(parent=item)
            is_active = current_url.startswith(item.get_url())
            menu.append({
                'item': item,
                'children': build_menu(children),
                'is_active': is_active,
                'is_parent': parent is None,
            })
        return menu

    menu_items = MenuItem.objects.filter(menu_name=menu_name).order_by('parent', 'order')
    menu_tree = build_menu(menu_items)
    return {'menu_tree': menu_tree}