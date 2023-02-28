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
    path('customers/update/<int:id>', views.update, name='update'),
    path('customers/update/updatecustomer/<int:id>', views.updatecustomer, name='updatecustomer'),

    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add2, name='add2'),
    path('employees/add/addemployee/', views.addemployee, name='addemployee'),
    path('employees/delete/<int:id>', views.delete2, name='delete2'),
    path('employees/update/<int:id>', views.update2, name='update2'),
    path('employees/update/updateemployee/<int:id>', views.updateemployee, name='updateemployee'),

    path('services/', views.services, name='services'),
    path('services/add/', views.add3, name='add3'),
    path('services/add/addservice/', views.addservice, name='addservice'),
    path('services/delete/<int:id>', views.delete3, name='delete3'),
    path('services/update/<int:id>', views.update3, name='update3'),
    path('services/update/updateservice/<int:id>', views.updateservice, name='updateservice'),
]
