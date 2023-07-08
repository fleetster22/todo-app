from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProjectSerializer
from .models import Project
from .forms import ProjectForm


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


@login_required
def list_projects(request):
    user = request.user
    members = Project.objects.filter(owner=user)
    context = {"list_projects": members}

    return render(request, "projects/project_list.html", context)


@login_required
def show_project(request, id=id):
    proj_details = get_object_or_404(Project, id=id)
    context = {"project_details": proj_details}

    return render(request, "projects/proj_details.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {"form": form}
    return render(request, "projects/create.html", context)
