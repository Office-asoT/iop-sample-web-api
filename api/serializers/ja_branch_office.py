from rest_framework import serializers

from api.models import JaBranchOffice

class JaBranchOfficePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = JaBranchOffice
        fields = [
            'name',
            'number',
            'zipcode',
            'address',
            'phone_number',
            'email_address',
        ]
