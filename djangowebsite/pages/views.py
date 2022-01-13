from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def register(response):
    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {'form':form})