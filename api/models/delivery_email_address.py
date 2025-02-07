from django.db import models

class DeliveryEmailAddress(models.Model):
    user_id = models.CharField('ユーザーID', max_length=254)
    delivery_name = models.CharField('宛先名称', max_length=254)
    email_address = models.CharField('メールアドレス', max_length=254)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'email_address'],
                name='unique_user_id_email_address'
            )
        ]
