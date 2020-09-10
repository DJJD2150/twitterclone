from django.shortcuts import HttpResponseRedirect, render, reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from twitteruser.models import TwitterUser
from authentication.forms import LoginForm, SignupForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            klutter_user = authenticate(
                request,
                username=data.get("username"),
                password=data.get("password")
            )
            if klutter_user:
                login(request, klutter_user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse("homepage"))
            )

    form = LoginForm()
    return render(request, "login_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_klutter_user = TwitterUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password")
            )
            # Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_klutter_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "signup_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

