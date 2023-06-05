from django.shortcuts import render, get_list_or_404
from projects.models import Project


def list_project(request):
    list_projects = get_list_or_404(Project)
    context = {"list_projects": list_projects}

    return render(request, "projects/project_list.html", context)
