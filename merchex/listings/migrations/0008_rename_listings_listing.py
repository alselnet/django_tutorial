# Generated by Django 5.0.4 on 2024-04-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_rename_type_listings_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]