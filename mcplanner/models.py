from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    title =models.CharField(max_length=100)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title