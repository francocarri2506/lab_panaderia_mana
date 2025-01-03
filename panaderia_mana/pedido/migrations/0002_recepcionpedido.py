# Generated by Django 5.1.2 on 2024-11-04 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_initial'),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecepcionPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField(auto_now_add=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('empleado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recepcion', to='pedido.pedido')),
            ],
        ),
    ]
