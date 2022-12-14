# Generated by Django 4.1.3 on 2022-11-28 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Convenio",
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
                ("nome", models.CharField(max_length=50)),
                ("n_carteira", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Paciente",
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
                ("nome", models.CharField(max_length=60)),
                ("data_nascimento", models.DateField()),
                ("cpf", models.CharField(max_length=12)),
                ("telefone", models.CharField(max_length=12)),
                (
                    "convenio",
                    models.ForeignKey(
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="paciente.convenio",
                    ),
                ),
            ],
        ),
    ]
