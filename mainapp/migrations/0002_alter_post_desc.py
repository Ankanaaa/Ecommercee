# Generated by Django 4.1.5 on 2023-02-01 11:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
