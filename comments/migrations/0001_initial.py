# Generated by Django 5.1.3 on 2024-11-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("comment_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_delete", models.BooleanField(default=False)),
            ],
        ),
    ]
