# Generated by Django 4.1.5 on 2023-03-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0008_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=48, verbose_name="Название поста"),
                ),
                ("text", models.TextField(max_length=448, verbose_name="Тело поста")),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("date_publication", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.new_profile",
                        verbose_name="Автор",
                    ),
                ),
            ],
        ),
    ]
