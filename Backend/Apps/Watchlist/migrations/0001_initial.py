# Generated by Django 5.0.1 on 2024-01-22 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Movie", "0001_initial"),
        ("User", "0002_alter_user_bio_alter_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Watchlist",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True)),
                ("isPublic", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="User.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovieInWatchlist",
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
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Movie.movie"
                    ),
                ),
                (
                    "watchlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Watchlist.watchlist",
                    ),
                ),
            ],
        ),
    ]
