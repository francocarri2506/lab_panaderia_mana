# Generated by Django 5.1.2 on 2024-10-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
