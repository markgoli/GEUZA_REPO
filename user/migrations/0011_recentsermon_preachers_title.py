# Generated by Django 5.0.1 on 2024-01-22 15:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_recentsermon_options_event_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentsermon',
            name='preachers_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
