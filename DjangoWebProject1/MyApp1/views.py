from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,MyApp1 Django")

# Create your views here.
