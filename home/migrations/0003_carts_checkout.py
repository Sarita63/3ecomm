# Generated by Django 4.0.4 on 2022-06-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_carts_items_carts_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
