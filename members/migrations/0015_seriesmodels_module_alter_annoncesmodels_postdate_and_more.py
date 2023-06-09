# Generated by Django 4.2 on 2023-05-18 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_annoncesmodels_postdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesmodels',
            name='module',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.modulemodels'),
        ),
        migrations.AlterField(
            model_name='annoncesmodels',
            name='postdate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 18, 17, 21, 17, 255967, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='annoncesmodels',
            name='updated',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 5, 18, 17, 21, 17, 255967, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
