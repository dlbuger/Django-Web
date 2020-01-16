import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from src.wrapper import allowed_users

from src import db_handler
from .forms import EmployeeRecord
# Create your views here.

def get_form(request):
    if request.method == 'POST':
        form = EmployeeRecord(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            db_handler.InsertBackend.append_employee(form.cleaned_data)
            messages.success(request, "员工添加成功!")
            return redirect('/new-employee')
    else:
        form = EmployeeRecord()
    return render(request, 'add_employee.html', {'form':form})