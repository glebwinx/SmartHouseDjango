# Generated by Django 3.2.9 on 2023-01-29 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_products_prod'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('number', models.CharField(max_length=20, verbose_name='Номер')),
                ('price', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Цена')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.products', verbose_name='Продукт')),
            ],
        ),
    ]
