# Generated by Django 4.2.3 on 2023-08-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]