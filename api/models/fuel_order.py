from django.db import models

from api.models import JaBranchOffice

class FuelOrder(models.Model):

    user_id = models.CharField('ユーザーID', max_length=254)
    farm_field_id = models.CharField('圃場ID', max_length=254)
    ja_branch_office = models.ForeignKey(JaBranchOffice, on_delete=models.CASCADE, verbose_name='店番号')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="発注日時")
    fuel_type = models.CharField(max_length=10, verbose_name="燃料種類")
    quantity = models.IntegerField(verbose_name="数量（L）")
    status = models.CharField(max_length=10, verbose_name="ステータス")
