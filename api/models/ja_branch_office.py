from django.db import models

class JaBranchOffice(models.Model):
    name = models.CharField('店舗名', max_length=254)
    number = models.CharField('店番号', max_length=3, unique=True)
    zipcode = models.CharField('郵便番号', max_length=7)
    address = models.CharField('住所', max_length=254)
    phone_number = models.CharField('電話番号', max_length=15)
    email_address = models.CharField('メールアドレス', max_length=254)
