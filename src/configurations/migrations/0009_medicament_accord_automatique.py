# Generated by Django 3.2.19 on 2023-06-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0008_alter_log_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='accord_automatique',
            field=models.BooleanField(default=False),
        ),
    ]
