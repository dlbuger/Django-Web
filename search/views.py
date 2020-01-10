from django.shortcuts import render
from django.shortcuts import HttpResponse
from .db_handler import search_by_contract, search_by_employee
from .forms import SearchInput

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    # ignore!
    context = {"text": "This is from context"}
    return render(request, 'index.html',context)

def search_result(request):
    context = None
    if request.method == 'GET':
        # if 'search_num' in dict(request.GET):
        result = request.GET.get('search_num')
        print(result)
        # if result is not None:
        context = {"dataframe": result}
        return HttpResponse(render(request,'employee.html',context))