# Generated by Django 2.1.2 on 2018-12-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0016_auto_20181128_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='telefono',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
