# Generated by Django 4.1.4 on 2022-12-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_info',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
