# Generated by Django 3.0.5 on 2021-06-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210606_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.FloatField(default=None),
        ),
    ]
