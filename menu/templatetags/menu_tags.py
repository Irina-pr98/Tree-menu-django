from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    # Получение элементов меню по имени
    items = MenuItem.objects.filter(parent__isnull=True).select_related('parent')
    return {'items': items, 'request': context['request']}