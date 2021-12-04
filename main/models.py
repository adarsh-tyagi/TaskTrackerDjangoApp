from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
# Task model
class Task(models.Model):
    title = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"