# Generated by Django 5.1.1 on 2024-09-05 14:32

import django.db.models.deletion
import sinistre.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("configurations", "0213_auto_20240903_1738"),
        ("sinistre", "0116_auto_20240822_0955"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="paiementcomptable",
            name="observation",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="paiementcomptable",
            name="statut_validite",
            field=models.CharField(
                choices=[
                    ("VALIDE", "Valide"),
                    ("SUPPRIME", "Supprime"),
                    ("BROUILLON", "Brouillon"),
                    ("CLOTURE", "Cloture"),
                ],
                default="VALIDE",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="date_ordonnancement",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="date_reglement",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="far",
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="net_regle",
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="numero_bordereau",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="numero_lettre_cheque",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="ticket_prefinance",
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name="sinistre",
            name="tps",
            field=models.DecimalField(decimal_places=16, max_digits=50, null=True),
        ),
        migrations.CreateModel(
            name="FactureCompagnie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero",
                    models.CharField(
                        blank=True,
                        default=sinistre.models.generate_random_invoice_number,
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("montant_total", models.BigIntegerField()),
                ("montant_regle", models.BigIntegerField(default=0, null=True)),
                ("montant_restant", models.BigIntegerField(null=True)),
                ("date_emission", models.DateField(blank=True, null=True)),
                (
                    "fichier",
                    models.FileField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="factures/fact_compagnies",
                    ),
                ),
                (
                    "statut",
                    models.CharField(
                        choices=[("SOLDE", "Solde"), ("NON SOLDE", "Non Solde")],
                        default="NON SOLDE",
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "statut_validite",
                    models.CharField(
                        choices=[
                            ("VALIDE", "Valide"),
                            ("SUPPRIME", "Supprime"),
                            ("BROUILLON", "Brouillon"),
                            ("CLOTURE", "Cloture"),
                        ],
                        default="VALIDE",
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "observation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bureau",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.bureau",
                    ),
                ),
                (
                    "compagnie",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.compagnie",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "devise",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.devise",
                    ),
                ),
            ],
            options={
                "verbose_name": "Facture d'une compagnie",
                "verbose_name_plural": "Factures des compagnies",
                "db_table": "facture_compagnie",
            },
        ),
        migrations.AddField(
            model_name="sinistre",
            name="facture_compagnie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="sinistre.facturecompagnie",
            ),
        ),
        migrations.CreateModel(
            name="ReglementCompagnie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "numero_piece",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "banque_emettrice",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "montant",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=20, null=True
                    ),
                ),
                ("date_reglement", models.DateField(blank=True, null=True)),
                ("observation", models.CharField(max_length=255, null=True)),
                ("motif_annulation", models.CharField(max_length=255, null=True)),
                (
                    "statut_validite",
                    models.CharField(
                        choices=[
                            ("VALIDE", "Valide"),
                            ("SUPPRIME", "Supprime"),
                            ("BROUILLON", "Brouillon"),
                            ("CLOTURE", "Cloture"),
                        ],
                        default="VALIDE",
                        max_length=15,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "banque",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.banque",
                    ),
                ),
                (
                    "bureau",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.bureau",
                    ),
                ),
                (
                    "compagnie",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.compagnie",
                    ),
                ),
                (
                    "compte_tresorerie",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.comptetresorerie",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "devise",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="configurations.devise",
                    ),
                ),
                (
                    "mode_reglement",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.modereglement",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reglement compagnie",
                "verbose_name_plural": "Reglements faits par les compagnies",
                "db_table": "reglement_compagnie",
            },
        ),
        migrations.CreateModel(
            name="ReglementFactureCompagnie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "montant_regle",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=20, null=True
                    ),
                ),
                ("observation", models.CharField(max_length=255, null=True)),
                (
                    "statut_validite",
                    models.CharField(
                        choices=[
                            ("VALIDE", "Valide"),
                            ("SUPPRIME", "Supprime"),
                            ("BROUILLON", "Brouillon"),
                            ("CLOTURE", "Cloture"),
                        ],
                        default="VALIDE",
                        max_length=15,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bureau",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="configurations.bureau",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "facture_compagnie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="sinistre.facturecompagnie",
                    ),
                ),
                (
                    "reglement_compagnie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="sinistre.reglementcompagnie",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reglement facture",
                "verbose_name_plural": "Reglement facture",
                "db_table": "reglement_facture_compagnie",
            },
        ),
    ]
