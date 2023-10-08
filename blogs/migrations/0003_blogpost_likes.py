# Generated by Django 4.2.5 on 2023-10-08 14:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0002_alter_blogpost_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]