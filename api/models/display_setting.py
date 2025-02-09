from django.db import models

class DisplaySetting(models.Model):
    user_id = models.CharField('ユーザーID', max_length=254)
    farm_field_id = models.CharField('圃場ID', max_length=254)
    setting = models.JSONField('表示設定', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'farm_field_id'],
                name='unique_display_setting'
            )
        ]
