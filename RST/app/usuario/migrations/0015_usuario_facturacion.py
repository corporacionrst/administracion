# Generated by Django 2.1.2 on 2018-11-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_auto_20181126_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='facturacion',
            field=models.BooleanField(default=False),
        ),
    ]