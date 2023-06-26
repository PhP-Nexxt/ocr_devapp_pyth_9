from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from litreview_app.forms import SignupForm
from litreview_app.forms import LoginForm


def user_login(request):  # Formulaire de connection
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(
                        "dashboard"
                    )  # Redirige vers la vue associée à l'URL 'dashboard'
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "litreview_app/login.html", {"form": form})


def user_register(request):  # Formulaire de création de compte
    form = SignupForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecter l'utilisateur après l'inscription
            login(request, user)
            return redirect(
                "dashboard"
            )  # Redirige vers la vue associée à l'URL 'dashboard'
        else:
            return HttpResponse("Registration failed")
    else:
        form = UserCreationForm()
    return render(request, "litreview_app/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("litreview_app/login.html")
