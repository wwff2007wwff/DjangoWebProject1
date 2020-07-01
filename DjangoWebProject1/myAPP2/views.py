from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,myAPP2 Django")

# Create your views here.
