from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import FormView
# Create your views here.
from .forms import ProgramRecord

def get_form(request):
    if request.method == 'POST':
        form = ProgramRecord(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            return HttpResponse("Success")
    else:
        form = ProgramRecord()

    return render(request, 'add.html',{'form':form})