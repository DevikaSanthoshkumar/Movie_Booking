# Generated by Django 5.0.2 on 2024-04-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(max_length=500),
        ),
    ]
