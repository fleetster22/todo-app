"""
URL configuration for tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from projects.views import ProjectView
from tasks.views import TaskView


router = routers.DefaultRouter()
router.register(r"projects", ProjectView, "project")
router.register(r"tasks", TaskView, "task")


# def redirect_to_user_login(request):
#     return redirect("user_login")


urlpatterns = [
    # path("", redirect_to_user_login, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("projects/", include("projects.urls")),
    path("accounts/", include("accounts.urls")),
    path("tasks/", include("tasks.urls")),
]
