# Generated by Django 3.0.4 on 2020-04-06 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='aotes',
            new_name='votes',
        ),
    ]
