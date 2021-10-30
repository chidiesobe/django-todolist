from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    datecreated = models.DateTimeField(auto_now_add=True)
    datecomplete = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title