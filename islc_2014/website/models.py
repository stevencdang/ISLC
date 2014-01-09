from django.db import models


# Create your models here.
SLCS = (('CELEST', 'CELEST'),
        ('LIFE', 'LIFE'),
        ('PSLC', 'PSLC'),
        ('SILC', 'SILC'),
        ('TDLC', 'TDLC'),
        ('VL2', 'VL2'))

STUDENT_STATUS = (('Undergraduate', 'Undergraduate'),
                  ('Graduate', 'Graduate'),
                  ('PostDoc', 'PostDoc'))
NON_RESEARCH_INTERESTS = (('None', 'None'),
                         ('Animals/Pets', 'Animals/Pets'),
                         ('Computers/Electronics', 'Computers/Electronics'),
                         ('Current Events/Politics', 'Current Events/Politics'),
                         ('Fine Arts/Reading', 'Fine Arts/Reading'),
                         ('Food/Wine', 'Food/Wine'),
                         ('Music/Dance', 'Music/Dance'),
                         ('Nature/Outdoors', 'Nature/Outdoors'),
                         ('Sports/Athletics', 'Sports/Athletics'),
                         ('Television/Movies', 'Television/Movies'))


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
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=254, default='')
    phone = models.CharField(max_length=20, null=True, blank=True, default='')
    status = models.CharField(max_length=30,
                              choices=STUDENT_STATUS, default='')
    slc = models.CharField(max_length=10, choices=SLCS, default='')
    department = models.CharField(max_length=100, default='')
    university = models.CharField(max_length=200, default='')
    research = models.TextField(null=True, blank=True)
    nr1 = models.CharField(max_length=30,
                           choices=NON_RESEARCH_INTERESTS, default='')
    nr2 = models.CharField(max_length=30,
                           choices=NON_RESEARCH_INTERESTS, default='')
    nr3 = models.CharField(max_length=30,
                           choices=NON_RESEARCH_INTERESTS, default='')
    diet = models.TextField(null=True, blank=True)
    special_needs = models.TextField(null=True, blank=True)
    picture = models.FileField(upload_to='ppl', default='default_face.jpg')
    abstract = models.TextField(null=True, blank=True, default='')
    symposium_talk = models.BooleanField(default=False)
    children_museum = models.BooleanField(default=False)
    child_museum_essay = models.TextField(null=True,
                                          blank=True,
                                          default='')
