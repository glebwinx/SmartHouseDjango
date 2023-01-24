# Generated by Django 3.2.9 on 2023-01-24 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_controler_packet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='prod',
        ),
        migrations.CreateModel(
            name='CreateAssembling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contr', models.ManyToManyField(related_name='asses', to='core.Controler', verbose_name='Контроллер')),
                ('produ', models.ManyToManyField(related_name='asses', to='core.Products', verbose_name='Устройство')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assemp', to='core.new_profile', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Assembling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField()),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assem', to='core.controler')),
                ('creass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assemp', to='core.createassembling')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assem', to='core.products')),
            ],
        ),
    ]