# Generated by Django 2.0 on 2018-12-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20181202_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='imei',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
