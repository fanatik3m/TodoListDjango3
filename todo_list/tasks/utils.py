class AddContextMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        return context