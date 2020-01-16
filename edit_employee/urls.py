from django.urls import path, include
from . import views



urlpatterns = [
    path('edit-employee/', views.edit_employee)
]