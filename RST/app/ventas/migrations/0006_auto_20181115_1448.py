# Generated by Django 2.1.2 on 2018-11-15 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20181114_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='autoriza',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='autoriza_compra', to='usuario.Usuario'),
        ),
    ]
