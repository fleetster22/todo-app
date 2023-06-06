from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project


@login_required
def list_projects(request):
    user = request.user
    list_project = Project.objects.filter(owner=user)
    context = {"list_projects": list_project}

    return render(request, "projects/project_list.html", context)
