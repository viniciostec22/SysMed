# Generated by Django 4.1.3 on 2022-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('especialidades', models.CharField(max_length=50)),
                ('crm', models.CharField(max_length=12)),
                ('cpf', models.CharField(max_length=11)),
                ('dta_nascimento', models.DateField()),
                ('tel', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=150)),
            ],
        ),
    ]
