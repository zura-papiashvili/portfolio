# Generated by Django 5.1.4 on 2025-01-31 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=255)),
                (
                    "description",
                    models.TextField(help_text="Detailed description of the project."),
                ),
                (
                    "customer_name",
                    models.CharField(help_text="Name of the customer.", max_length=255),
                ),
                (
                    "customer_email",
                    models.EmailField(
                        help_text="Customer's email address.", max_length=254
                    ),
                ),
                (
                    "customer_phone",
                    models.CharField(
                        blank=True,
                        help_text="Customer's phone number.",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "start_date",
                    models.DateField(help_text="The date the project started."),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True,
                        help_text="The estimated or actual completion date of the project.",
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("planning", "Planning"),
                            ("in_progress", "In Progress"),
                            ("completed", "Completed"),
                            ("on_hold", "On Hold"),
                        ],
                        default="planning",
                        help_text="Current status of the project.",
                        max_length=20,
                    ),
                ),
                (
                    "budget",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Total budget allocated for the project.",
                        max_digits=10,
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Total cost incurred so far (optional).",
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Image related to the project.",
                        null=True,
                        upload_to="project_images/",
                    ),
                ),
                (
                    "project_video",
                    models.URLField(
                        blank=True,
                        help_text="Link to a video of the project (optional).",
                        null=True,
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Additional notes about the project.",
                        null=True,
                    ),
                ),
            ],
            options={
                "ordering": ["-start_date"],
            },
        ),
    ]
