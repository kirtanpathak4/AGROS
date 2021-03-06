# Generated by Django 3.2 on 2021-04-17 11:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210405_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.farmer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
