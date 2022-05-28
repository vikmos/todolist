from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    """Класс для заданий"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    create_date = models.DateTimeField(default=timezone.now)
    task_status = models.BooleanField(default=False)

    def create_task(self):
        self.create_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
