# Generated by Django 3.2.15 on 2023-12-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0108_alter_paramacte_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paramacte',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
