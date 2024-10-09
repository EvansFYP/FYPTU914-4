from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime

from .models import User



def signup(request):
    if request.method == "GET":
        context = {}
        return render(request, "webapp/signup.html", context)
    else:
        user = User.objects.create_user(
            username=request.POST["Username"],
            password=request.POST["Password"]
        )
        
        return HttpResponseRedirect(reverse("webapp:signin"))

def signin(request):
    if request.method == "GET":
        context = {}
        return render(request, "webapp/signin.html", context)
    else:
        user = authenticate(
            request,
            username=request.POST["Username"],
            password=request.POST["Password"]
        )

        if user is not None:
            login(request, user)
            print("logged in", user)
            return HttpResponseRedirect(reverse("webapp:home"))

def home(request):
    if request.method == "GET":
        context = {}
        return render(request, "webapp/home.html", context) 
