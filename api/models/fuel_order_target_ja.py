from django.db import models

from api.models import JaBranchOffice

class FuelOrderTargetJa(models.Model):
    user_id = models.CharField('ユーザーID', max_length=254)
    farm_field_id = models.CharField('圃場ID', max_length=254)
    ja_branch_office = models.ForeignKey(JaBranchOffice, on_delete=models.CASCADE, verbose_name='店番号')
