# Generated by Django 3.2.19 on 2023-07-02 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sinistre', '0009_prorogationsinistre'),
    ]

    operations = [
        migrations.AddField(
            model_name='prorogationsinistre',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
