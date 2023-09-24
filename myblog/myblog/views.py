from django.http import HttpResponse
from django.shortcuts import render




def details(request):
    return render(request,"Home.html")

def update(request):
    return render(request,"title.html")

    