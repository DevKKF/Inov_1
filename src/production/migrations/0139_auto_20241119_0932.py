# Generated by Django 3.2.15 on 2024-11-19 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0229_businessunit'),
        ('production', '0138_rename_created_by_secteuractivite_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secteuractivite',
            options={'verbose_name': "Secteur d'activité ", 'verbose_name_plural': "Secteur d'activité"},
        ),
        migrations.AddField(
            model_name='client',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='configurations.businessunit'),
        ),
        migrations.AlterModelTable(
            name='secteuractivite',
            table='secteur_activite',
        ),
    ]
