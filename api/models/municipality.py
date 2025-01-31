from django.db import models

class Municipality(models.Model):
    code = models.CharField('市町村コード', max_length=10, unique=True)
    name = models.CharField('市町村名', max_length=254)
    latitude = models.FloatField('緯度')
    longitude = models.FloatField('経度')
    zipcode = models.CharField('郵便番号', max_length=7)
    address = models.CharField('住所', max_length=254)
