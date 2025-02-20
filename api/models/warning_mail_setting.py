from django.db import models
import uuid

class WarningMailSetting(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField('ユーザーID', max_length=254)
    farm_field_id = models.CharField('圃場ID', max_length=254)
    warning_name = models.CharField('警報名称', max_length=254)
    monitoring_start_time = models.TimeField('監視開始時刻')
    monitoring_end_time = models.TimeField('監視終了時刻')
    monitoring_sensor = models.CharField('監視センサー', max_length=254)
    monitoring_condition = models.CharField('監視条件', max_length=254)
    monitoring_value = models.FloatField('監視数値')
    duration = models.PositiveSmallIntegerField('継続時間（分）')
    enabled = models.BooleanField('有効')
