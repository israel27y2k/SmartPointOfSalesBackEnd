# Generated by Django 4.0.4 on 2022-07-01 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellido del cliente')),
                ('correo', models.CharField(max_length=200, verbose_name='Correo del cliente')),
                ('dirección', models.CharField(max_length=200, null=True, verbose_name='Dirección del cliente')),
            ],
        ),
    ]
