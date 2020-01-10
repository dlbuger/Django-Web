from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def modify(request):
    return HttpResponse("<h1>Modify</h1>")
