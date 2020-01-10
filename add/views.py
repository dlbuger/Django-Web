from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request):
    return HttpResponse("<h1>添加新的记录</h1>")