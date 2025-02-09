from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import DisplaySetting
from api.serializers import DisplaySettingPublicSerializer

BASE_SETTING = {
    'home': {
        'current-value': {
          'air_temperature': True,
          'relative_humidity': True,
          'co2_concentration': True,
          'solar_irradiance': True,
        },
        'environment-graph': {
          'air_temperature': True,
          'relative_humidity': True,
          'co2_concentration': True,
          'solar_irradiance': True,
        },
    },
}

class DisplaySettingList(APIView):

    def get(self, request, user_id):
        display_settings = DisplaySetting.objects.filter(user_id=user_id).all()
        if len(display_settings) == 0:
            DisplaySetting.objects.bulk_create([
                DisplaySetting(user_id=user_id, farm_field_id='farm-field-a', setting=BASE_SETTING),
                DisplaySetting(user_id=user_id, farm_field_id='farm-field-b', setting=BASE_SETTING),
                DisplaySetting(user_id=user_id, farm_field_id='farm-field-c', setting=BASE_SETTING),
            ])
            display_settings = DisplaySetting.objects.filter(user_id=user_id).all()
        serializer = DisplaySettingPublicSerializer(display_settings, many=True)
        return Response(serializer.data)
