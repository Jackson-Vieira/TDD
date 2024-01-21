from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseNotAllowed
from django.urls import reverse

from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "task/index.html", {"tasks": tasks})


def detail(request, id: int):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, "task/detail.html", {"task": task})


def delete(request, id: int):
    if request.method == "POST":
        try:
            task = Task.objects.get(pk=id)
            task.delete()
        except Task.DoesNotExist:
            raise Http404("Task does not exist")
        return redirect(reverse("task:list_tasks"))
    else:
        return HttpResponseNotAllowed(["POST"])
