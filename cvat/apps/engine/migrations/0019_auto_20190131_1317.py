# Generated by Django 2.1.5 on 2019-01-31 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0018_auto_20190131_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientfile',
            old_name='path',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='remotefile',
            old_name='path',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='serverfile',
            old_name='path',
            new_name='file',
        ),
    ]