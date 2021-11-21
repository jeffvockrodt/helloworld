from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Here's a new change I made")
# Create your views here.
