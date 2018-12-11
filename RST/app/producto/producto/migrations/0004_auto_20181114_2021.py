# Generated by Django 2.1.2 on 2018-11-14 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_usuario_crear_proveedor'),
        ('producto', '0003_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('costo', models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True)),
                ('distribuidor', models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True)),
                ('mayorista', models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True)),
                ('efectivo', models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True)),
                ('tarjeta', models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Lista')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Tienda')),
            ],
        ),
        migrations.AlterField(
            model_name='codigo',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_a_lista', to='producto.Lista'),
        ),
    ]