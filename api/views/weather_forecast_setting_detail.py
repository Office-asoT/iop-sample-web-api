from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from api.models import WeatherForecastSetting
from api.serializers import WeatherForecastSettingPublicSerializer, WeatherForecastSettingUpdateSerializer

class WeatherForecastSettingDetail(APIView):

    def get(self, request, user_id):
        weather_forecast_setting = WeatherForecastSetting.objects.filter(user_id=user_id).first()
        if not weather_forecast_setting:
            raise Http404
        serializer = WeatherForecastSettingPublicSerializer(weather_forecast_setting)
        return Response(serializer.data)

    def post(self, request):
        pass

    def patch(self, request, user_id):
        weather_forecast_setting = WeatherForecastSetting.objects.filter(user_id=user_id).first()
        if not weather_forecast_setting:
            raise Http404

        serializer = WeatherForecastSettingUpdateSerializer(weather_forecast_setting, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(WeatherForecastSettingPublicSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
