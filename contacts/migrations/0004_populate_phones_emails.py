from django.db import migrations
from contacts.worker import populate_phones_emails
from contacts.models import Person


def populate(apps, schema_editor):
    persons = Person.objects.all()
    populate_phones_emails(persons)


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_populate_persons'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
