# Generated by Django 3.0.4 on 2020-04-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voters',
            field=models.ManyToManyField(blank=True, null=True, to='forum.Voter'),
        ),
    ]