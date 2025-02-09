from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from api.models import DisplaySetting
from api.serializers import DisplaySettingPublicSerializer, DisplaySettingUpdateSerializer

class DisplaySettingDetail(APIView):

    def get(self, request, user_id, farm_field_id):
        display_setting = DisplaySetting.objects.filter(user_id=user_id, farm_field_id=farm_field_id).first()
        if not display_setting:
            raise Http404
        serializer = DisplaySettingPublicSerializer(display_setting)
        return Response(serializer.data)

    def patch(self, request, user_id, farm_field_id):
        display_setting = DisplaySetting.objects.filter(user_id=user_id, farm_field_id=farm_field_id).first()
        if not display_setting:
            raise Http404

        serializer = DisplaySettingUpdateSerializer(display_setting, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(DisplaySettingPublicSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
