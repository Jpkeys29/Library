from django.shortcuts import render
#To return a simple "It's working" import HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("It's working!")