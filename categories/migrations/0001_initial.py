# Generated by Django 5.1.3 on 2024-11-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=50)),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
