# Generated by Django 5.0 on 2023-12-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productmodel_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='title',
        ),
    ]