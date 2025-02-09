from rest_framework import serializers

from api.models import FuelOrderTargetJa, JaBranchOffice
from api.serializers import JaBranchOfficePublicSerializer

class FuelOrderTargetJaPublicSerializer(serializers.ModelSerializer):
    ja_branch_office = JaBranchOfficePublicSerializer()

    class Meta:
        model = FuelOrderTargetJa
        fields = [
            'farm_field_id',
            'ja_branch_office'
        ]

class FuelOrderTargetJaCreateSerializer(serializers.ModelSerializer):
    # JaBranchOffice = JaBranchOfficePublicSerializer()
    class Meta:
        model = FuelOrderTargetJa
        fields = ['user_id', 'farm_field_id', 'ja_branch_office']

class FuelOrderTargetJaUpdateSerializer(serializers.ModelSerializer):
    ja_branch_office_number = serializers.CharField(write_only=True)

    class Meta:
        model = FuelOrderTargetJa
        fields = ['farm_field_id', 'ja_branch_office_number']

    def update(self, instance, validated_data):
        ja_branch_office_number = validated_data.pop('ja_branch_office_number', None)
        if ja_branch_office_number:
            try:
                validated_data["ja_branch_office"] = JaBranchOffice.objects.get(number=ja_branch_office_number)
            except JaBranchOffice.DoesNotExist:
                raise serializers.ValidationError({"detail": "指定された number のJA店舗は存在しません。"})
        return super().update(instance, validated_data)
