from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_completed', 'time_create', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content', 'user')
    list_editable = ('is_completed',)
    list_filter = ('is_completed', 'time_create', 'user')


admin.site.register(Task, TaskAdmin)