# Generated by Django 5.1.4 on 2025-02-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_webproduct_description_en_webproduct_description_es_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="main",
            field=models.BooleanField(default=False, verbose_name="Main FAQ"),
        ),
    ]
