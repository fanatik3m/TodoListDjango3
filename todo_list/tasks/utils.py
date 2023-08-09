# menu = [
#         {'title': 'Main Page', 'url_name': 'index'},
#     ]
menu = []


class AddContextMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu.copy()
        return context