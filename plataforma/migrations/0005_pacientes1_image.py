# Generated by Django 4.2 on 2023-05-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_alter_documentos_options_documentos_fecha_subida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]