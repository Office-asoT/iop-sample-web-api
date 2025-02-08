from rest_framework import serializers

from api.models import DisplaySetting

class DisplaySettingPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplaySetting
        fields = [
            'farm_field_id',
            'setting'
        ]

class DisplaySettingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplaySetting
        fields = [
            'user_id',
            'farm_field_id',
            'setting'
        ]
