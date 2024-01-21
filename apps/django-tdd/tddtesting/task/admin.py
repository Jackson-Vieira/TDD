from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    ...

admin.site.register(Task, TaskAdmin)
