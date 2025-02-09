from rest_framework import serializers

from api.models import FuelOrder
from api.serializers import JaBranchOfficePublicSerializer

class FuelOrderListPublicSerializer(serializers.ModelSerializer):
    ja_branch_office = JaBranchOfficePublicSerializer()

    class Meta:
        model = FuelOrder
        fields = [
            'farm_field_id',
            'ja_branch_office',
            'order_date',
            'fuel_type',
            'quantity',
            'status'
        ]
