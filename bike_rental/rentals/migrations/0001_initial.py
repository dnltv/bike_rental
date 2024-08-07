# Generated by Django 5.0.8 on 2024-08-07 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Велосипед',
                'verbose_name_plural': 'Велосипеды',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.bike')),
            ],
        ),
    ]