# Generated by Django 2.1.2 on 2018-11-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_usuario_cargar_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='orden_de_compra',
            field=models.BooleanField(default=False),
        ),
    ]
