# Generated by Django 5.1.2 on 2024-10-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=250)),
                ('telefono', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('domicilioCalle', models.CharField(max_length=200)),
                ('domicilioNumero', models.IntegerField()),
                ('domicilioLocalidad', models.CharField(max_length=200)),
                ('domicilioDepartamento', models.CharField(max_length=200)),
            ],
        ),
    ]