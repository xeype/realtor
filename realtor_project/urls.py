"""realtor_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from realtor_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add, name='add'),
    path('customers/add/addcustomer/', views.addcustomer, name='addcustomer'),
    path('customers/delete/<int:id>', views.delete, name='delete'),
    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add2, name='add2'),
    path('employees/add/addemployee/', views.addemployee, name='addemployee'),
]
