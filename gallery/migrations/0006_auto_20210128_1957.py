# Generated by Django 3.1.5 on 2021-01-29 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200328_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='address',
            name='postalCodeExt',
        ),
        migrations.AlterField(
            model_name='address',
            name='postalCode',
            field=models.CharField(max_length=11),
        ),
    ]
