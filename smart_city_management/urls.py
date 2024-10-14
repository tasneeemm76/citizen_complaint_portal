"""
URL configuration for smart_city_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.reg, name='register'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('report_issue/', views.report_issue, name='report_issue'),
    path('emergency_services/', views.emergency, name='emergency'),
    path('heatmap/',views.heatmap_view,name='heatmap'),
    path('dashboard/',views.admin_dashboard,name='dashboard'),
    path('analysis/',views.search_by_area,name='analysis'),
]
