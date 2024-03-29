# Generated by Django 4.1.5 on 2023-04-01 06:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "__first__"),
        ("smarthouseblog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                    "condition",
                    models.TextField(max_length=12, verbose_name="Cостояние"),
                ),
                ("date_order", models.DateTimeField(auto_now_add=True)),
                (
                    "date_dilivery",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="products", to="smarthouseblog.blog"
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.new_profile",
                    ),
                ),
            ],
        ),
    ]
