# Generated by Django 4.2 on 2023-04-09 22:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promptbook', '0009_category_help_text'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prompt',
            unique_together={('text', 'owner', 'category')},
        ),
    ]