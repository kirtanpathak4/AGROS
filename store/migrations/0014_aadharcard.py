# Generated by Django 3.0.6 on 2021-04-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210312_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aadharcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_card_no', models.CharField(max_length=20)),
            ],
        ),
    ]