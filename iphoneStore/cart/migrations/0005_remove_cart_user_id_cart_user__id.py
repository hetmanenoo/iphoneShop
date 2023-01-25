# Generated by Django 4.1.4 on 2023-01-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_items_auth_update_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_user',
            name='id',
        ),
        migrations.AddField(
            model_name='cart_user',
            name='_id',
            field=models.AutoField(default=0, editable=False, primary_key=True, serialize=False, verbose_name='Id'),
            preserve_default=False,
        ),
    ]
