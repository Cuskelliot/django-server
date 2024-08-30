from django.shortcuts import render
from django.http import HttpResponse

# request -> response handler
# Create your views here.


def hello(request):
    return HttpResponse("hello")
