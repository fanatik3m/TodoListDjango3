class AddContextMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        return context