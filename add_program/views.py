import sys
sys.path.append("..")
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView
from django.contrib import messages


from src import db_handler
from .forms import ProgramRecord

def get_form(request):
    if request.method == 'POST':
        form = ProgramRecord(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            db_handler.InsertBackend.append_program(form.cleaned_data)
            messages.success(request, "提交成功")
            return redirect('/new-program')
    else:
        form = ProgramRecord()

    return render(request, 'add_program.html',{'form':form})
