# Generated by Django 2.0 on 2018-12-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20181204_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='chennai',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]