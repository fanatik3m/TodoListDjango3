from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterUserForm, LoginUserForm, AddTaskForm, EditTaskFieldsForm
from .utils import AddContextMixin
from .models import Task


class MainPageView(AddContextMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Main Page')
        return {**context, **user_context}

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id).select_related('user')


class RegisterUser(AddContextMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Зарегистрироваться')
        return {**context, **user_context}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(AddContextMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tasks/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title='Войти')
        return {**context, **user_context}

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                Task.objects.create(**data, user_id=request.user.id)
                return redirect('index')
            except Exception as ex:
                print(ex)
    else:
        form = AddTaskForm()

    context = {
        'form': form,
        'title': 'Добавить задачу'
    }

    return render(request, 'tasks/register.html', context=context)


@login_required
def task_detail(request, user, task_slug):
    if request.user.username != user:
        raise PermissionDenied()

    task = Task.objects.get(user_id=request.user.id, slug=task_slug)
    context = {
        'title': f'{task.title}',
        'task': task
    }
    return render(request, 'tasks/detail_task.html', context=context)


def edit_status_task(request, user, task_slug):
    if request.method == 'POST':
        if request.user.username != user:
            return HttpResponseForbidden()

        task = Task.objects.get(user_id=request.user.id, slug=task_slug)
        task.is_completed = request.POST.get('is_completed') == 'on'
        task.save()
        return redirect('index')
    else:
        return HttpResponseNotAllowed('POST')


def delete_task(request, user, task_slug):
    if request.user.username != user:
        return HttpResponseForbidden()

    task = Task.objects.get(user_id=request.user.id, slug=task_slug)
    task.delete()
    return redirect('index')


def edit_task_fields(request, user, task_slug):
    if request.user.username != user:
        return HttpResponseForbidden()

    task = Task.objects.get(user_id=request.user.id, slug=task_slug)
    if request.method == 'POST':
        form = EditTaskFieldsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.title = data.get('title')
            task.description = data.get('description')
            task.slug = data.get('slug')
            task.is_completed = data.get('is_completed')
            try:
                task.save()
            except Exception as ex:
                print(ex)
            return redirect('index')
    else:
        form = EditTaskFieldsForm(instance=task)

    context = {
        'title': 'Изменить задачу',
        'form': form
    }

    return render(request, 'tasks/register.html', context=context)