# Generated by Django 5.0.4 on 2024-04-26 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listings_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
