from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
import sys
sys.path.append("..")
from src.db_handler import SearchBackend as sb
from src.wrapper import allowed_users
from .db_handler import search_by_contract, search_by_employee, employee_record
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
@allowed_users(allow=['root','读取员工'])
def employee_search_result(request, id):
    if id is not None:
        if id in sb.employee_record():
            df = sb.search_by_employee(id)
            return render(request, 'employee/employee.html', df)
        else:
            messages.error(request,'没有这个记录!')
            return redirect('/')

@login_required
@allowed_users(allow=['Root','读取项目'])
def program_search_result(request, id):
    if id is not None:
        if id in sb.program_record():
            df = sb.search_by_contract(id)
            print(df)
            return render(request, 'program/program.html',df)
        else: 
            messages.error(request, '没有这个记录')
            return redirect('/')