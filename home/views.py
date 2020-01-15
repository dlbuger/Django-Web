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
@allowed_users(allow=['Root'])
def search_result(request, id):
    print(request.user.groups.all()[0].name)
    if id is not None:
        if id in sb.employee_record():
            df = sb.search_by_employee(id).to_dict('records')[0]
            return render(request, 'employee.html', df)
        else:
            messages.error(request,'没有这个记录!')
            return redirect('/')
