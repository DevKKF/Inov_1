# Generated by Django 3.2.15 on 2024-06-08 12:17

import configurations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0179_paramacte_delais_carence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='tarfile',
            field=models.FileField(blank=True, default=None, null=True, upload_to=configurations.models.upload_location_bureau),
        ),
    ]
