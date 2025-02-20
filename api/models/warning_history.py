from django.db import models

class WarningHistory(models.Model):
    user_id = models.CharField('ユーザーID', max_length=254)
    farm_field_id = models.CharField('圃場ID', max_length=254)
    warning_name = models.CharField('警報名称', max_length=254)
    warning_date_time = models.DateTimeField('監視開始時刻')
