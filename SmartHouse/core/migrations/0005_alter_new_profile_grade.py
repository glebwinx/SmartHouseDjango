# Generated by Django 3.2.9 on 2023-01-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230119_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_profile',
            name='grade',
            field=models.IntegerField(verbose_name='Оценка'),
        ),
    ]