from django.db import models

# Create your models here.

# for modeling each item in the todo list
# inherits models.Model from django
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
