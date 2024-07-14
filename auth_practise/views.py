from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.shortcuts import redirect, render

from .forms import EditUserForm, RegisterForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created successfully")
            form.save(commit=True)
            print(form.cleaned_data)

            return redirect("profile")

    else:
        form = RegisterForm()

    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Login in successful")
                return redirect("profile")
            else:
                messages.error(request, "Something Went Wrong")
                return redirect("signup")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.error(request, "Logged Out Successfully")
    return redirect("login")


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect("profile")
    else:
        messages.error(request, "Password Change Failed")
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})


def forget_password(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect("profile")
    else:

        form = SetPasswordForm(user=request.user)
    return render(request, "change_password.html", {"form": form})


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                print("Edit Profile", form.cleaned_data)
                messages.success(request, "Profile Updated Successfully")
                return redirect("profile")
        else:

            form = EditUserForm(instance=request.user)
        return render(request, "edit_profile.html", {"form": form})
