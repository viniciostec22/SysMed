# Generated by Django 4.1.3 on 2022-12-11 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
        ('consulta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcarconsulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico'),
        ),
    ]