# Generated by Django 5.0.2 on 2024-04-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0005_booking_film_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='time1',
            field=models.CharField(default='11:30', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='time2',
            field=models.CharField(default='11:30', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='time3',
            field=models.CharField(default='11:30', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='time4',
            field=models.CharField(default='11:30', max_length=50),
        ),
    ]