from . import views
from django.urls import path

app_name = "task"

urlpatterns = [
    path("", views.index, name="list_tasks"),
    path("<int:id>", views.detail, name="task_detail"),
    path("<int:id>/delete", views.delete, name="task_delete"),
]
