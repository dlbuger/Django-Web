from django.urls import path, include
from . import views



urlpatterns = [
    path('new-program/', views.get_form)
]