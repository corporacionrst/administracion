# Generated by Django 2.1.2 on 2018-11-15 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20181115_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
