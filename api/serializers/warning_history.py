from rest_framework import serializers

from api.models import WarningHistory

class WarningHistoryPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningHistory
        fields = [
            'farm_field_id',
            'warning_name',
            'warning_date_time',
        ]
