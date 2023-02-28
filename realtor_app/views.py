from django.db import connection
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


def delete(request, id):
    member = Customers.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('customers'))


def employees(request):
    my_employees = Employees.objects.all().values()
    template = loader.get_template('all_employees.html')
    context = {
        'employees': my_employees
    }
    return HttpResponse(template.render(context, request))


def add2(request):
    template = loader.get_template('add_employee.html')
    return HttpResponse(template.render({}, request))


def addemployee(request):
    fn = request.POST['first_name']
    sn = request.POST['second_name']
    pn = request.POST['phone_number']
    ad = request.POST['address']
    member = Employees(first_name=fn, second_name=sn, phone_number=pn, address=ad)
    member.save()
    return HttpResponseRedirect(reverse('employees'))


def update2(request, id):
    employee = Employees.objects.get(id=id)
    template = loader.get_template('update_employee.html')
    context = {
        'employee': employee
    }
    return HttpResponse(template.render(context, request))


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


def delete2(request, id):
    member = Employees.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('employees'))


def services(request):
    query = 'SELECT a.id, a.service_name, b.price FROM realtor_app_services a, realtor_app_prices b WHERE a.price_id = b.id;'
    with connection.cursor() as cursor:
        cursor.execute(query)
        my_objects = cursor.fetchall()
    template = loader.get_template('all_services.html')
    context = {
        'objects': my_objects
    }
    return HttpResponse(template.render(context, request))


def add3(request):
    template = loader.get_template('add_service.html')
    return HttpResponse(template.render({}, request))


def addservice(request):
    sn = request.POST['service_name']
    p = request.POST['price']

    price = Prices(price=p)
    price.save()

    get_price = Prices.objects.filter(price=p)
    pid = get_price.latest('id').id

    service = Services(service_name=sn, price_id=pid)
    service.save()
    return HttpResponseRedirect(reverse('services'))


def update3(request, id):
    service = Services.objects.get(id=id)
    template = loader.get_template('update_service.html')
    context = {
        'service': service
    }
    return HttpResponse(template.render(context, request))


def updateservice(request, id):
    sn = request.POST['service_name']
    p = request.POST['price']

    service = Services.objects.get(id=id)

    pid = service.price_id

    service.service_name = sn
    service.save()

    prices = Prices.objects.get(id=pid)
    prices.price = p
    prices.save()

    return HttpResponseRedirect(reverse('services'))


def delete3(request, id):
    service = Services.objects.get(id=id)
    service.delete()
    return HttpResponseRedirect(reverse('services'))
