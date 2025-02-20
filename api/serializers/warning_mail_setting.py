from rest_framework import serializers

from api.models import WarningMailSetting

class WarningMailSettingPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningMailSetting
        fields = '__all__'

class WarningMailSettingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningMailSetting
        fields = [
            'user_id',
            'farm_field_id',
            'warning_name',
            'monitoring_start_time',
            'monitoring_end_time',
            'monitoring_sensor',
            'monitoring_condition',
            'monitoring_value',
            'duration',
            'enabled',
        ]

class WarningMailSettingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningMailSetting
        fields = [
            'enabled',
        ]
