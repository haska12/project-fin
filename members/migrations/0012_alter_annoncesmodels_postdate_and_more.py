# Generated by Django 4.2 on 2023-05-15 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_alter_annoncesmodels_postdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annoncesmodels',
            name='postdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 15, 15, 3, 54, 700710, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='annoncesmodels',
            name='updated',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 15, 15, 3, 54, 700710, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
