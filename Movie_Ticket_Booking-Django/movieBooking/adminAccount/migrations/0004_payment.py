# Generated by Django 5.0.2 on 2024-04-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminAccount', '0003_booking_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=100)),
                ('amount', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]