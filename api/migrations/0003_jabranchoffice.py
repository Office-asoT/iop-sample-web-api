# Generated by Django 5.1.5 on 2025-02-08 07:55
from django.db import migrations, models
import csv
from api.models import JaBranchOffice

def add_initial_data(apps, schema_editor):
    Ja_branch_offices = []
    with open ('./ja_branch_office.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Ja_branch_offices.append(JaBranchOffice(
                name=row['name'],
                number=row['number'],
                zipcode=row['zipcode'],
                address=row['address'],
                phone_number=row['phone_number'],
                email_address=row['email_address'],
            ))
    JaBranchOffice.objects.bulk_create(Ja_branch_offices)

def remove_initial_data(apps, schema_editor):
    apps.get_model('api', 'JaBranchOffice').objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_deliveryemailaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='JaBranchOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='店舗名')),
                ('number', models.CharField(max_length=3, unique=True, verbose_name='店番号')),
                ('zipcode', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=254, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=15, verbose_name='電話番号')),
                ('email_address', models.CharField(max_length=254, verbose_name='メールアドレス')),
            ],
        ),
        migrations.RunPython(add_initial_data,remove_initial_data)
    ]

    
