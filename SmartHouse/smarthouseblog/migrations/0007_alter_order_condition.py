# Generated by Django 3.2.9 on 2023-04-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthouseblog', '0006_remove_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='condition',
            field=models.TextField(default='Передано на сборку', max_length=12, verbose_name='Cостояние'),
        ),
    ]
