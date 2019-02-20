from faker import Factory
from random import choice, randint, sample
from .models import Person, Address, Phone, Group, Email, CONTACT_TYPES

GROUPS = (
    (1, 'Rodzina'),
    (2, 'Znajomi'),
    (3, 'Praca'),
    (4, 'Uczelnia'),
)


def fake_address():
    fake = Factory.create(locale='pl')

    a = Address()

    a.country = fake.country()
    a.street = fake.street_name()
    a.number = int(fake.building_number().split('/')[0])
    a.zipcode = fake.postcode()
    a.city = fake.city()
    a.aptNumber = int(fake.random_digit_not_null())

    print(a)
    a.save()


def fake_person(addresses):
    fake = Factory.create(locale='pl')

    p = Person()

    p.firstName = fake.first_name()
    p.lastName = fake.last_name()
    p.description = fake.sentence()
    p.company = fake.company()
    p.job = fake.job()
    p.address = choice(addresses)

    print(p)
    p.save()


def fake_phone(persons):
    fake = Factory.create(locale='pl')

    ph = Phone()
    ph.phoneNumber = fake.phone_number().replace(' ', '')
    ph.phoneType = choice(CONTACT_TYPES)[0]
    ph.person = choice(persons)

    print(ph)
    ph.save()


def fake_email(persons):
    fake = Factory.create(locale='pl')

    em = Email()
    em.email = fake.email()
    em.emailType = choice(CONTACT_TYPES)[0]
    em.person = choice(persons)

    print(em)
    em.save()


def fake_group(name, persons):

    gr = Group()
    gr.name = name

    print(gr)
    gr.save()

    gr.person.set(persons)


def populate_addresses():

    for i in range(0, 50):
        fake_address()


def populate_persons(addresses_list):
    for i in range(0, 100):
        fake_person(addresses_list)


def populate_phones_emails(persons_list):
    for i in range(0, 100):
        fake_phone(persons_list)
        fake_email(persons_list)

    for group in GROUPS:
        name = group[1]
        fake_group(name, sample(list(persons_list), 30))
