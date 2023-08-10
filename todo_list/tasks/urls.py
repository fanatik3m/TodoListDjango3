from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('task/', add_task, name='add_task'),
    path('task_detail/<user>/<slug:task_slug>/', task_detail, name='task_detail'),
    path('edit/<user>/<slug:task_slug>', edit_status_task, name='edit_task'),
    path('delete/<user>/<slug:task_slug>', delete_task, name='delete_task'),
    path('edit_full/<user>/<slug:task_slug>', edit_task_fields, name='edit_task_fields')
]