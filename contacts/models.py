from django.db import models
from django_countries.fields import CountryField

# Create your models here.

CONTACT_TYPES = (
    (1, 'Cell'),
    (2, 'Work'),
    (3, 'Home'),
    (4, 'Main'),
    (5, 'Fax-home'),
    (6, 'Fax-work'),
    (7, 'Other'),
)

class Person(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=64)
    description = models.CharField(max_length=200, null=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)
    company = models.CharField(max_length=100, null=True)
    job = models.CharField(max_length=100, null=True)

class Address(models.Model):
    country = CountryField()
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
    aptNumber = models.PositiveSmallIntegerField(null=True)

class Phone(models.Model):
    phoneNumber = models.PositiveSmallIntegerField()
    phoneType = models.SmallIntegerField(choices=CONTACT_TYPES)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

class Email(models.Model):
    email = models.EmailField()
    emailType = models.SmallIntegerField(choices=CONTACT_TYPES)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    person = models.ManyToManyField('Person')

