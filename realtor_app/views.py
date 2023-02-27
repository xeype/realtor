from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Customers, Employees, Services, Prices
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


def delete(request, id):
    member = Customers.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('customers'))


def delete2(request, id):
    member = Employees.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('employees'))


def addcustomer(request):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Customers(first_name=fn, second_name=sn, phone_number=pn, address=ad)
    member.save()
    return HttpResponseRedirect(reverse('customers'))


def update(request, id):
    customer = Customers.objects.get(id=id)
    template = loader.get_template('update_customer.html')
    context = {
        'customer': customer
    }
    return HttpResponse(template.render(context, request))


def update2(request, id):
    employee = Employees.objects.get(id=id)
    template = loader.get_template('update_employee.html')
    context = {
        'employee': employee
    }
    return HttpResponse(template.render(context, request))


def updatecustomer(request, id):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Customers.objects.get(id=id)
    member.first_name = fn
    member.second_name = sn
    member.phone_number = pn
    member.address = ad
    member.save()
    return HttpResponseRedirect(reverse('customers'))


def updateemployee(request, id):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Employees.objects.get(id=id)
    member.first_name = fn
    member.second_name = sn
    member.phone_number = pn
    member.address = ad
    member.save()
    return HttpResponseRedirect(reverse('employees'))


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


def services(request):
    # query = "SELECT a.id, a.service_name, b.price FROM realtor_app_services a, realtor_app_prices b WHERE a.price_id = b.id;"
    # my_services = Services.objects.raw(query)
    my_services = Services.objects.filter().select_related('price_id').query
    template = loader.get_template('all_services.html')
    context = {
        'services': my_services
    }
    return HttpResponse(template.render(context, request))
