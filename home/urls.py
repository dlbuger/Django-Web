from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index),
    path('search/result/<int:id>/', views.employee_search_result),
    path('search/result/<str:id>/', views.program_search_result)
]