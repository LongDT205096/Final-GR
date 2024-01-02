# Generated by Django 4.2.4 on 2023-12-27 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("born", models.CharField(max_length=100)),
                ("image_url", models.CharField(max_length=200)),
                ("biography", models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name="actorVideo",
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
                ("url", models.CharField(max_length=200)),
                ("duration", models.IntegerField()),
                (
                    "actors",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actors_video",
                        to="actors.actor",
                    ),
                ),
            ],
        ),
    ]
