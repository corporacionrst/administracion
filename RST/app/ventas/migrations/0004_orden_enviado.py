# Generated by Django 2.1.2 on 2018-11-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_venta_hoja'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='enviado',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
