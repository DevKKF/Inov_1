# Generated by Django 3.2.15 on 2024-05-28 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0174_merge_20240527_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compagnie',
            name='has_taux_multiple',
        ),
    ]
