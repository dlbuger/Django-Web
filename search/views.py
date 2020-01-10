from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from .db_handler import search_by_contract, search_by_employee, employee_record
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


def search_result(request, id):
    if id is not None:
        if id in employee_record():
            df = search_by_employee(id).to_dict('records')[0]
            return HttpResponse(render(request, 'employee.html', df))
    else:
        return render(request,'index.html')

def redirect_2_index(request):
    response = redirect('/')
    return response