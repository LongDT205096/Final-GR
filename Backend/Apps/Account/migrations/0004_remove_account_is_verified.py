# Generated by Django 5.0.1 on 2024-01-05 05:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Account", "0003_account_is_verified"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="is_verified",
        ),
    ]
