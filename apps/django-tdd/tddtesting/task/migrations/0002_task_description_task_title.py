# Generated by Django 5.0.1 on 2024-01-18 23:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="title",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
