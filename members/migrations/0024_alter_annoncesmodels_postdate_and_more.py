# Generated by Django 4.2 on 2023-05-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_alter_annoncesmodels_postdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annoncesmodels',
            name='postdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='annoncesmodels',
            name='updated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
