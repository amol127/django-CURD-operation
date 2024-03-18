from django.shortcuts import redirect, render
from django.http import HttpResponse



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def serview(request):
    return render(request, "services.html")
