from rest_framework import serializers

from api.models import WeatherForecastSetting, Municipality
from api.serializers import MunicipalityPublicSerializer

class WeatherForecastSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecastSetting
        fields = '__all__'

class WeatherForecastSettingPublicSerializer(serializers.ModelSerializer):
    municipality = MunicipalityPublicSerializer()

    class Meta:
        model = WeatherForecastSetting
        fields = ['municipality']

class WeatherForecastSettingUpdateSerializer(serializers.ModelSerializer):
    municipality_code = serializers.CharField(write_only=True)

    class Meta:
        model = WeatherForecastSetting
        fields = ['municipality_code']

    def update(self, instance, validated_data):
        municiaplity_code = validated_data.pop('municipality_code', None)
        if municiaplity_code:
            try:
                instance.municipality = Municipality.objects.get(code=municiaplity_code)
            except Municipality.DoesNotExist:
                raise serializers.ValidationError({"detail": "指定された code の市町村は存在しません。"})
        return super().update(instance, validated_data)
