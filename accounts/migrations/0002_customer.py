# Generated by Django 3.1.6 on 2021-02-19 08:05

import core.utils.functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "code",
                    models.CharField(
                        db_index=True,
                        default=core.utils.functions.unique_code,
                        max_length=5,
                        unique=True,
                    ),
                ),
                ("phone", models.CharField(default="254", max_length=12)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
