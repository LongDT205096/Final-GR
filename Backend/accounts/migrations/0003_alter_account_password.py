# Generated by Django 4.2.4 on 2023-12-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_account_options_alter_account_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="password",
            field=models.CharField(max_length=256),
        ),
    ]