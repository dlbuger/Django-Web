from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index),
    path('search/result/<int:id>/', views.search_result),
    path('search/result/', views.redirect_2_index)
]