# Generated by Django 5.0.1 on 2024-01-12 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_event_addresss_alter_event_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='geolocation',
        ),
    ]
