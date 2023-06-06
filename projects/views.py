from django.shortcuts import render, get_list_or_404
from projects.models import Project


def list_projects(request):
    list_project = get_list_or_404(Project)
    context = {"list_projects": list_project}

    return render(request, "projects/project_list.html", context)
