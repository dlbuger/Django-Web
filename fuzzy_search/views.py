from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fuzzy_search(request):
    return HttpResponse("<h1>模糊搜索</h1>")