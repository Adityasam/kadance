# Generated by Django 2.0 on 2018-10-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_distribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='center_id',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
