from statistics import mode
from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email_address = models.EmailField(max_length=100, null=True)
    login = models.TextField(max_length=100)
    password = models.TextField(max_length=100)


class priorities(models.Model):
    name_priority = models.TextField(max_length=50)
    number = models.IntegerField()


class tasks(models.Model):
    name_task = models.TextField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField()
    is_execute = models.BooleanField()
    priority = models.ForeignKey(priorities, on_delete=models.PROTECT)
    user = models.ForeignKey(users, on_delete=models.CASCADE) 
