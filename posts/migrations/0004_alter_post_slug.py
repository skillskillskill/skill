# Generated by Django 5.1.3 on 2024-11-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=100),
        ),
    ]