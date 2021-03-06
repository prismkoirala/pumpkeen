# Generated by Django 3.1.2 on 2020-10-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=100)),
                ('price', models.DecimalField(decimal_places='3', max_digits='6')),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=100)),
                ('quantity', models.IntegerField(default='1')),
                ('oil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.oiltype')),
            ],
        ),
    ]
