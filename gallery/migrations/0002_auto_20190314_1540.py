# Generated by Django 2.1.4 on 2019-03-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
