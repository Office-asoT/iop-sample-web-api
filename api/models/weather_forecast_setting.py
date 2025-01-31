from django.db import models

from api.models import Municipality

class WeatherForecastSetting(models.Model):
    user_id = models.CharField('ユーザーID', max_length=254, unique=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, verbose_name='市町村')
