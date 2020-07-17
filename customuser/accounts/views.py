from django.shortcuts import render
from django.contrib.auth import login, logout, get_user_model
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        user_obj = form.cleaned_data.get("user_obj")
        login(request, user_obj)
        return HttpResponseRedirect("/")
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")
