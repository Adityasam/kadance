# Generated by Django 2.0 on 2018-12-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20181202_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='tablet_id',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
