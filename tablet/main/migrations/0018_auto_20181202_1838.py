# Generated by Django 2.0 on 2018-12-02 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20181202_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='end_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='start_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]