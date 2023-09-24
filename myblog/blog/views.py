from django.http import HttpResponse
from django.shortcuts import render
from blog.models import blog

def list(request):
    return render(request,"index.html")

def details(request):
    return render(request,"Home.html")

