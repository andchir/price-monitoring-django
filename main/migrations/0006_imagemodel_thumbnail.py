# Generated by Django 5.0 on 2024-01-02 10:43

import django_advance_thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_productmodel_price_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='thumbnail',
            field=django_advance_thumbnail.fields.AdvanceThumbnailField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]