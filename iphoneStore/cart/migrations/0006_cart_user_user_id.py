# Generated by Django 4.1.4 on 2023-01-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_cart_user_id_cart_user__id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_user',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]