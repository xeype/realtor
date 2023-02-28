from django.db import models


# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()


class Employees(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()


class Prices(models.Model):
    price = models.FloatField()


class Services(models.Model):
    service_name = models.CharField(max_length=255)
    price = models.ForeignKey(Prices, on_delete=models.CASCADE)


class Apartments(models.Model):
    num_of_rooms = models.IntegerField()
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(Employees, on_delete=models.CASCADE)
    price = models.ForeignKey(Prices, on_delete=models.CASCADE)


class Agreements(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
