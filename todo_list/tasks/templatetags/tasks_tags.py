from django import template

options = (
    {'name': 'time_update', 'label': 'Время последнего изменения'},
    {'name': 'time_create', 'label': 'Время создания'},
    {'name': 'is_completed', 'label': 'Выполненные'},
    {'name': 'is_uncompleted', 'label': 'Невыполненные'}
)

register = template.Library()


@register.inclusion_tag('tasks/list_mainmenu.html', name='show_mainmenu')
def show_menu_tag():
    menu = [
        {'title': 'Добавить задачу', 'url_name': 'add_task'},
    ]

    return {'menu': menu}


@register.inclusion_tag('tasks/list_filter_form.html', name='show_filters')
def show_filters():
    return {'options': options}