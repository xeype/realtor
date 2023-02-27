from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Customers, Employees
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


def add2(request):
    template = loader.get_template('add_employee.html')
    return HttpResponse(template.render({}, request))


def addcustomer(request):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Customers(first_name=fn, second_name=sn, phone_number=pn, address=ad)
    member.save()
    return HttpResponseRedirect(reverse('customers'))


def employees(request):
    my_employees = Employees.objects.all().values()
    template = loader.get_template('all_employees.html')
    context = {
        'employees': my_employees
    }
    return HttpResponse(template.render(context, request))


def addemployee(request):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Employees(first_name=fn, second_name=sn, phone_number=pn, address=ad)
    member.save()
    return HttpResponseRedirect(reverse('employees'))
