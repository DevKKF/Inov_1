# Generated by Django 3.2.15 on 2024-04-16 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sinistre', '0097_historiqueordonnancementsinistre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historiqueordonnancementsinistre',
            old_name='borderau_ordonnancement',
            new_name='bordereau_ordonnancement',
        ),
    ]
