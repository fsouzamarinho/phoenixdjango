# Generated by Django 5.1.1 on 2024-11-29 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("material", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Roupa",
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
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "descricao",
                    models.TextField(blank=True, null=True, verbose_name="Descrição"),
                ),
                ("imagem", models.ImageField(upload_to="fotos/")),
            ],
        ),
        migrations.CreateModel(
            name="RoupaMaterial",
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
                ("quantidade", models.PositiveBigIntegerField()),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="material.material",
                    ),
                ),
                (
                    "roupa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="roupa.roupa"
                    ),
                ),
            ],
        ),
    ]
