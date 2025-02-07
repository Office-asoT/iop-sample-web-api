from rest_framework import serializers

from api.models import DeliveryEmailAddress

class DeliveryEmailAddressPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryEmailAddress
        fields = [
            'delivery_name',
            'email_address'
        ]

class DeliveryEmailAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryEmailAddress
        fields = ['user_id', 'delivery_name', 'email_address']

class DeliveryEmailAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryEmailAddress
        fields = ['delivery_name']
