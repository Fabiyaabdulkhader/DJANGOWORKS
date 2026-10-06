from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#function based

def home(request):

    return HttpResponse("wellcome to Django")


#viewname index

def index(request):

    return HttpResponse("Index Page")
