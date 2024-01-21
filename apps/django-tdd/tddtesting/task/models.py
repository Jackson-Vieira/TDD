from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
