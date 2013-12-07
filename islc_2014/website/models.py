from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Address(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)


class Email(models.Model):
    address = models.CharField(max_length=100)


class Phone(models.Model):
    home = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    cell = models.CharField(max_length=20)


class Registration(models.Model):
    attendee = models.ForeignKey(Person)
    address = models.ForeignKey(Address)
    email = models.ForeignKey(Email)
    phone = models.ForeignKey(Phone)
