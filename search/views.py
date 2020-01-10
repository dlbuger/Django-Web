from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
from .db_handler import search_by_contract, search_by_employee, employee_record
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


def search_result(request, id):
    if id is not None:
        if id in employee_record():
            df = search_by_employee(id).to_dict('records')[0]
            return render(request, 'employee.html', df)
        else:
            messages.error(request,'没有这个记录!')
            return redirect('/')