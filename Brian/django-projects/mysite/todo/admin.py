from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Todo)
admin.site.register(models.Note)