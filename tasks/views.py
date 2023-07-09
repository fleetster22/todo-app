from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .forms import TaskForm
from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {"form": form}
    return render(request, "tasks/create.html", context)


def show_my_tasks(request):
    user = request.user
    tasks = Task.objects.filter(assignee=user)
    context = {"tasks": tasks}
    return render(request, "tasks/my_tasks.html", context)
