# Generated by Django 3.1.2 on 2020-10-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0009_auto_20201003_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinghistory',
            name='total',
            field=models.IntegerField(default=100),
        ),
    ]
