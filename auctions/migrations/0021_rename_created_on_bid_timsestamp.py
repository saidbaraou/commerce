# Generated by Django 5.1.3 on 2025-04-09 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_bid_listing_alter_bid_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='created_on',
            new_name='timsestamp',
        ),
    ]
