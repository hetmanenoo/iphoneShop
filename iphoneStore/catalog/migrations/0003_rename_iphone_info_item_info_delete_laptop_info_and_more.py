# Generated by Django 4.1.4 on 2023-01-05 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_iphone_info_laptop_info_watch_info_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='iphone_info',
            new_name='item_info',
        ),
        migrations.DeleteModel(
            name='laptop_info',
        ),
        migrations.DeleteModel(
            name='watch_info',
        ),
    ]
