# Generated by Django 2.1.1 on 2018-10-06 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181002_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirQuality',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('air_quality_level', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Decibel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('decibel_level', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('humidity_level', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pressure_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Location')),
            ],
        ),
    ]