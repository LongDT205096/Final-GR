# Generated by Django 5.0.1 on 2024-02-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Account", "0005_alter_account_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="name",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
