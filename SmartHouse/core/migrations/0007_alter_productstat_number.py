# Generated by Django 3.2.9 on 2023-01-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_productstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstat',
            name='number',
            field=models.CharField(max_length=8, verbose_name='Номер'),
        ),
    ]
