from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Task


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'slug')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class EditTaskFieldsForm(AddTaskForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'slug', 'is_completed')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }