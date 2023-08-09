from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm
from .utils import AddContextMixin


def index(request):
    context = {
        'title': 'Main Page',
        'menu': [
            {'title': 'About website', 'url_name': 'register'},
        ]
    }

    return render(request, 'tasks/index.html', context=context)


class RegisterUser(AddContextMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Register')
        return {**context, **user_context}


class LoginUser(AddContextMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tasks/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Log in')
        return {**context, **user_context}

    def get_success_url(self):
        return reverse_lazy('index')