# Generated by Django 4.1.7 on 2024-02-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("promptbook", "0013_category_pinned_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="help_text",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]