from django.urls import path
from projects.views import list_project

urlpatterns = [
    path("", list_project, name="list_projects"),
]
