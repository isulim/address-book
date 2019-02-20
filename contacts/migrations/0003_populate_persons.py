from django.db import migrations
from contacts.worker import populate_persons
from contacts.models import Address


def populate(apps, schema_editor):
    addresses = Address.objects.all()
    populate_persons(addresses)


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_populate_addresses'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
