# Generated by Django 2.2.13 on 2020-07-29 16:39

import arvestust.models.abstracts.file
import arvestust.models.validators.file
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arvestust', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage='packager.storage.PublicFileStorage', upload_to=arvestust.models.abstracts.file.file_upload_path, validators=[arvestust.models.validators.file.validate_file_size, arvestust.models.validators.file.validate_file_type], verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.CharField(max_length=64, unique=True, verbose_name='content'),
        ),
    ]
