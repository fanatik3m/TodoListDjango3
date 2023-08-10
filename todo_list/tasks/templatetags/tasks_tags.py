from django import template

register = template.Library()


@register.inclusion_tag('tasks/list_mainmenu.html', name='show_mainmenu')
def show_menu_tag():
    menu = [
        {'title': 'Добавить задачу', 'url_name': 'add_task'},
    ]

    return {'menu': menu}