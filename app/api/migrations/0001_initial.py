# Generated by Django 4.2 on 2023-04-11 09:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200, unique=True)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
