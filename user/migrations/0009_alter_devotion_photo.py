# Generated by Django 5.0.1 on 2024-01-22 13:08

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devotion',
            name='photo',
            field=models.ImageField(upload_to=user.models.get_image_upload_path),
        ),
    ]
