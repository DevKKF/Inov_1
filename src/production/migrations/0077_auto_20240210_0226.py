# Generated by Django 3.2.15 on 2024-02-10 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0152_auto_20240210_0151'),
        ('production', '0076_alter_reglement_quittance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reglement',
            name='operation',
        ),
        migrations.AddField(
            model_name='reglement',
            name='compte_tresorerie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.comptetresorerie'),
        ),
    ]
