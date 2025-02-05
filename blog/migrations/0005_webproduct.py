# Generated by Django 5.1.4 on 2025-02-05 14:41

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_author_bio_en_author_bio_es_author_bio_ka_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebProduct",
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
                ("name", models.CharField(max_length=100, verbose_name="Product Name")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="web_products/images",
                        validators=[blog.models.validate_image_size],
                        verbose_name="Image",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Available"),
                ),
            ],
            options={
                "verbose_name": "Web Product",
                "verbose_name_plural": "Web Products",
            },
        ),
    ]
