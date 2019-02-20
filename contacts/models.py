from django.db import models

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

    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName)


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
    aptNumber = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.country, self.city, self.street, self.number)


class Phone(models.Model):
    phoneNumber = models.CharField(max_length=16)
    phoneType = models.SmallIntegerField(choices=CONTACT_TYPES)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.person, self.phoneNumber)


class Email(models.Model):
    email = models.EmailField()
    emailType = models.SmallIntegerField(choices=CONTACT_TYPES)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.person, self.email)


class Group(models.Model):
    name = models.CharField(max_length=100)
    person = models.ManyToManyField('Person')

    def __str__(self):
        return self.name

