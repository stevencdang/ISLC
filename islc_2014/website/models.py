from django.db import models


# Create your models here.
SLCS = (('CELEST', 'CELEST'),
        ('LIFE', 'LIFE'),
        ('PSLC', 'PSLC'),
        ('SILC', 'SILC'),
        ('TDLC', 'TDLC'),
        ('VL2', 'VL2'))

STUDENT_STATUS = (('UG', 'Undergraduate'),
                  ('G', 'Graduate'),
                  ('P', 'PostDoc'))


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
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, default='')
    phone = models.CharField(max_length=20, null=True, blank=True, default='')
    status = models.CharField(max_length=30, choices=STUDENT_STATUS, blank=True, default='')
    slc = models.CharField(max_length=10, choices=SLCS, blank=True, default='')
    department = models.CharField(max_length=100, blank=True, default='')
    university = models.CharField(max_length=200, blank=True, default='')
    research = models.TextField(null=True, blank=True)
    diet = models.TextField(null=True, blank=True)
