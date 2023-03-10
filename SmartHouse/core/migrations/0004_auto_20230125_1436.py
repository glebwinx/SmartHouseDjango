# Generated by Django 3.2.9 on 2023-01-25 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_products_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='core.new_profile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='assembling',
            name='user',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='assem', to='core.new_profile', verbose_name='Пользователь'),
        ),
    ]
