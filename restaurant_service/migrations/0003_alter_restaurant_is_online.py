# Generated by Django 4.2.7 on 2023-11-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_service", "0002_alter_restaurant_is_online"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
    ]