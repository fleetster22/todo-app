from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from accounts.forms import LoginForm, SignUpForm


# validates user before loggin in, otherwise to "home"
def user_login(request):
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "GET":
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            # checks validity of password
            if password == password_confirmation:
                # Create a new user with those values
                # and save it to a variable

                user = User.objects.create_user(
                    username,
                    password=password,
                )
                # Log in the user with the user just created
                login(request, user)

                return redirect("list_projects")
            else:
                form.add_error("password", "the passwords do not match")

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
