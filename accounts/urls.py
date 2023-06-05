from django.urls import path
from accounts.views import user_login

urlpatterns = [
    path("accounts/", user_login, name="login"),
]
