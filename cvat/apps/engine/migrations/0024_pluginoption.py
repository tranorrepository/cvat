# Generated by Django 2.1.5 on 2019-02-05 18:17

import cvat.apps.engine.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0023_plugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PluginOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', cvat.apps.engine.models.SafeCharField(max_length=32)),
                ('value', cvat.apps.engine.models.SafeCharField(max_length=1024)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Plugin')),
            ],
        ),
    ]