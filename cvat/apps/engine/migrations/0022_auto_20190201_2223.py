# Generated by Django 2.1.5 on 2019-02-01 19:23

import cvat.apps.engine.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0021_task_image_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=cvat.apps.engine.models.upload_path_handler),
        ),
        migrations.AlterField(
            model_name='task',
            name='image_quality',
            field=models.PositiveSmallIntegerField(),
        ),
    ]