from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def edit_employee(request):
	return HttpResponse("修改员工")
