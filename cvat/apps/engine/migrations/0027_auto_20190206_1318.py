# Generated by Django 2.1.5 on 2019-02-06 10:18

import cvat.apps.engine.models
from django.db import migrations, models
import re
import csv
from io import StringIO

def parse_attribute(value):
    match = re.match(r'^([~@])(\w+)=(\w+):(.+)?$', value)
    if match:
        prefix = match.group(1)
        input_type = match.group(2)
        name = match.group(3)
        if match.group(4):
            values = list(csv.reader(StringIO(match.group(4)),
                quotechar="'"))[0]
        else:
            values = []

        return {'prefix':prefix, 'type':input_type, 'name':name, 'values':values}
    else:
        return None

def split_text_attribute(apps, schema_editor):
    AttributeSpec = apps.get_model('engine', 'AttributeSpec')
    for attribute in AttributeSpec.objects.all():
        spec = parse_attribute(attribute.text)
        if spec:
            attribute.mutable = (spec['prefix'] == '~')
            attribute.input_type = spec['type']
            attribute.name = spec['name']
            attribute.default_value = spec['values'][0]
            attribute.values = '\n'.join(spec['values'])
            attribute.save()

def join_text_attribute(apps, schema_editor):
    AttributeSpec = apps.get_model('engine', 'AttributeSpec')
    for attribute in AttributeSpec.objects.all():
        attribute.text = ""
        if attribute.mutable:
            attribute.text += "~"
        else:
            attribute.text += "@"

        attribute.text += attribute.input_type
        attribute.text += "=" + attribute.name + ":"
        attribute.text += ",".join(attribute.values.split('\n'))
        attribute.save()

class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0026_auto_20190206_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='source',
        ),
        migrations.AddField(
            model_name='attributespec',
            name='default_value',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributespec',
            name='input_type',
            field=models.CharField(choices=[('CHECKBOX', 'checkbox'), ('RADIO', 'radio'), ('NUMBER', 'number'), ('TEXT', 'text'), ('SELECT', 'select')], default='select', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributespec',
            name='mutable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributespec',
            name='name',
            field=models.CharField(default='test', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attributespec',
            name='values',
            field=models.CharField(default='', max_length=4096),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('ANNOTATION', 'annotation'), ('VALIDATION', 'validation'), ('COMPLETED', 'completed')], default=cvat.apps.engine.models.StatusChoice('annotation'), max_length=32),
        ),
        migrations.RunPython(split_text_attribute, join_text_attribute),
        migrations.RemoveField(
            model_name='attributespec',
            name='text',
        ),
        migrations.AlterUniqueTogether(
            name='attributespec',
            unique_together={('label', 'name')},
        ),
    ]