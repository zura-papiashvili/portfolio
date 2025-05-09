# Generated by Django 5.1.4 on 2025-02-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0004_remove_project_notes_en_remove_project_notes_es_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "title_en",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_es",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_ka",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "price_range",
                    models.CharField(max_length=255, verbose_name="Price Range"),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "description_en",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "description_es",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "description_ka",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "features",
                    models.TextField(
                        help_text="Separate features with a new line.",
                        verbose_name="Features",
                    ),
                ),
                (
                    "features_en",
                    models.TextField(
                        help_text="Separate features with a new line.",
                        null=True,
                        verbose_name="Features",
                    ),
                ),
                (
                    "features_es",
                    models.TextField(
                        help_text="Separate features with a new line.",
                        null=True,
                        verbose_name="Features",
                    ),
                ),
                (
                    "features_ka",
                    models.TextField(
                        help_text="Separate features with a new line.",
                        null=True,
                        verbose_name="Features",
                    ),
                ),
                (
                    "ideal_for",
                    models.TextField(
                        help_text="Separate target groups with a new line.",
                        verbose_name="Ideal For",
                    ),
                ),
                (
                    "ideal_for_en",
                    models.TextField(
                        help_text="Separate target groups with a new line.",
                        null=True,
                        verbose_name="Ideal For",
                    ),
                ),
                (
                    "ideal_for_es",
                    models.TextField(
                        help_text="Separate target groups with a new line.",
                        null=True,
                        verbose_name="Ideal For",
                    ),
                ),
                (
                    "ideal_for_ka",
                    models.TextField(
                        help_text="Separate target groups with a new line.",
                        null=True,
                        verbose_name="Ideal For",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
    ]
