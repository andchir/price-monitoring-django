# Generated by Django 5.0 on 2024-01-03 14:08

import django_advance_thumbnail.fields
import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_imagemodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=False, quality=85, scale=1, size=[1920, 1080], upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='thumbnail',
            field=django_advance_thumbnail.fields.AdvanceThumbnailField(blank=True, null=True, upload_to='thumbnails/%Y/%m/%d/'),
        ),
    ]