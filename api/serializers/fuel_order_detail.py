from rest_framework import serializers

from api.models import FuelOrder,JaBranchOffice

class FuelOrderCreateSerializer(serializers.ModelSerializer):
    ja_branch_office_number = serializers.CharField(write_only=True)
    class Meta:
        model = FuelOrder
        fields = [
            'user_id',
            'farm_field_id',
            'ja_branch_office',
            'order_date',
            'fuel_type', 
            'quantity',
            'status'
        ]
    def create(self, validated_data):
        ja_branch_office_number = validated_data.pop('ja_branch_office_number', None)
        try:
            ja_branch_office = JaBranchOffice.objects.get(number=ja_branch_office_number)
        except JaBranchOffice.DoesNotExist:
            raise serializers.ValidationError({"ja_branch_office_number": "指定された店番号の店舗が存在しません。"})

        validated_data['ja_branch_office'] = ja_branch_office
        return super().create(validated_data)

class FuelOrderStatusUpdateSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(write_only=True)
    order_date = serializers.DateTimeField(write_only=True)

    class Meta:
        model = FuelOrder
        fields = ['user_id', 'order_date', 'status']
