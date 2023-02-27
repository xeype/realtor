from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.TextField()
