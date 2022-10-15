from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Person(models.Model):
    user_name = models.CharField(max_length=150)
    first_name = models.CharField(blank=True, max_length=150)
    last_name = models.CharField(blank=True, max_length=150)
    email = models.EmailField(blank=True, max_length=150)
    password = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField(primary_key=False)
    is_superuser = models.BooleanField(primary_key=False)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name

class Event(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=150)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField()
    date_of_reg = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name




