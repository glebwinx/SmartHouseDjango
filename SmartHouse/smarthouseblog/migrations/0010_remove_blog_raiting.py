# Generated by Django 4.1.5 on 2023-03-21 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("smarthouseblog", "0009_blog_raiting"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="raiting",
        ),
    ]