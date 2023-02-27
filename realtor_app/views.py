from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Customers
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def customers(request):
    my_customers = Customers.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'customers': my_customers
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add_customer.html')
    return HttpResponse(template.render({}, request))


def addcustomer(request):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Customers(first_name=fn, second_name=sn, phone_number=pn, address=ad)
    member.save()
    return HttpResponseRedirect(reverse('customers'))
