from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return HttpResponse("Wow <strong>a</strong>")


def about(request):
    return HttpResponse("About us!")
