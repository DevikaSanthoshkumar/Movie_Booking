# Generated by Django 5.0.2 on 2024-04-06 05:57

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(default='unknown', max_length=150)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('is_enabled', models.BooleanField(default=True)),
                ('ticket_price', models.DecimalField(decimal_places=2, default=150, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('11:30', '11:30 am'), ('2:30', '2:30 pm'), ('5:00', '5:00 pm'), ('9:00', '9:00 pm')], default='11:30', max_length=50)),
                ('no_of_seats', models.IntegerField()),
                ('ticket_price', models.IntegerField(default=150)),
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminAccount.movie')),
            ],
        ),
    ]
