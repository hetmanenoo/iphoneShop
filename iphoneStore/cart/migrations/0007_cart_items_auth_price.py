# Generated by Django 4.1.4 on 2023-01-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cart_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_items_auth',
            name='price',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]