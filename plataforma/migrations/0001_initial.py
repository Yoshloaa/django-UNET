# Generated by Django 4.1.7 on 2023-03-31 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacientes1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=30)),
                ('apellidoM', models.CharField(max_length=30)),
                ('Fecha_na', models.DateField()),
            ],
        ),
    ]
