# Generated by Django 5.1.5 on 2025-01-31 06:06

import django.db.models.deletion
from django.db import migrations, models

import csv
from api.models import Municipality, WeatherForecastSetting

def add_initial_data(apps, schema_editor):
    municipalities = []
    with open ('./municipality.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            municipalities.append(Municipality(
                code=row['code'],
                name=row['name'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                zipcode=row['zipcode'],
                address=row['address'],
            ))
    Municipality.objects.bulk_create(municipalities)
    WeatherForecastSetting.objects.create(user_id='hoge', municipality_id=1).save()

def remove_initial_data(apps, schema_editor):
    WeatherForecastSetting.objects.all().delete()
    Municipality.objects.all().delete()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='市町村コード')),
                ('name', models.CharField(max_length=254, verbose_name='市町村名')),
                ('latitude', models.FloatField(verbose_name='緯度')),
                ('longitude', models.FloatField(verbose_name='経度')),
                ('zipcode', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=254, verbose_name='住所')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherForecastSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=254, unique=True, verbose_name='ユーザーID')),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.municipality', verbose_name='市町村')),
            ],
        ),
        migrations.RunPython(add_initial_data, remove_initial_data)
    ]
