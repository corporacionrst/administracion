# Generated by Django 2.1.2 on 2018-11-28 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0016_auto_20181128_1931'),
        ('traslado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traslados',
            name='usuario',
        ),
        migrations.AddField(
            model_name='traslados',
            name='despacha',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='despachada', to='usuario.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traslados',
            name='solicita',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='solicita', to='usuario.Usuario'),
            preserve_default=False,
        ),
    ]
