# Generated by Django 2.1.5 on 2019-02-05 10:07

import cvat.apps.engine.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0022_auto_20190201_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('name', models.SlugField(max_length=32, primary_key=True, serialize=False)),
                ('description', cvat.apps.engine.models.SafeCharField(max_length=8192)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('maintainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maintainers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]