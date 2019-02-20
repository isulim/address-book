from django.db import migrations
from contacts.worker import populate_addresses


def populate(apps, schema_editor):
    populate_addresses()


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
