from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        full_name = request.POST["full_name"]
        contact = request.POST["contact"]
        email = request.POST["email"]
        branch = request.POST["branch"]
        year = request.POST["year"]

        user = User.objects.create_user(username=username, password=password, email=email)
        Profile.objects.create(
            user=user,
            full_name=full_name,
            contact_number=contact,
            branch=branch,
            year=year
        )
        return redirect("login")

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
