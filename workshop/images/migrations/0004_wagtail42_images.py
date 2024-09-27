# Generated by Django 3.2.18 on 2023-03-02 13:25

from django.db import migrations

import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0003_wagtail30_streamfield_use_json_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height", width_field="width"
            ),
        ),
        migrations.AlterField(
            model_name="rendition",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height", width_field="width"
            ),
        ),
    ]
