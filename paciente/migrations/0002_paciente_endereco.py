# Generated by Django 4.1.3 on 2022-11-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("paciente", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="paciente",
            name="endereco",
            field=models.CharField(default="", max_length=200),
        ),
    ]
