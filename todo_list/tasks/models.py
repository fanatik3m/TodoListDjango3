from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_slug': self.slug})

    class Meta:
        unique_together = ('slug', 'user')
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['time_create', 'title']