# Generated by Django 3.0.4 on 2020-04-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200401_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='Author',
            field=models.CharField(max_length=50),
        ),
    ]
