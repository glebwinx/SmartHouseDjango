# Generated by Django 4.1.5 on 2023-03-21 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("smarthouseblog", "0008_delete_raiting"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="raiting",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="smarthouseblog.comments",
                verbose_name="Рейтинг",
            ),
            preserve_default=False,
        ),
    ]
