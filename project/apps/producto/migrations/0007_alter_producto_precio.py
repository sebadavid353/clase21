# Generated by Django 4.2.3 on 2023-08-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
