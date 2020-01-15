"""jason_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# 功能

from modify.views import modify # 修改
from fuzzy_search.views import fuzzy_search #模糊搜索



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('add_program.urls')),
    path('accounts/', include('login.urls')),
]

urlpatterns += staticfiles_urlpatterns()
