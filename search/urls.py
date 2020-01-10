from django.urls import path, include
from .views import search, index
from . import views



urlpatterns = [
    path('', index, name='index'),
    path('search/', views.search, name='search'),
    path('search/result/',views.search_result, name='search-result')
]