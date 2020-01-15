from django.urls import path, include
from . import views



urlpatterns = [
    path('new-employee/', views.get_form)
]