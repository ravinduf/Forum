# Generated by Django 3.0.4 on 2020-04-20 08:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(),
        ),
    ]