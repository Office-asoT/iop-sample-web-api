from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.models import WarningMailSetting
from api.serializers import WarningMailSettingPublicSerializer, WarningMailSettingUpdateSerializer

class WarningMailSettingDetail(APIView):

    def patch(self, request, user_id, pk):
        warning_mail_setting = get_object_or_404(WarningMailSetting, pk=pk)
        serializer = WarningMailSettingUpdateSerializer(warning_mail_setting, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(WarningMailSettingPublicSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, pk):
        warning_mail_setting = get_object_or_404(WarningMailSetting, pk=pk)
        warning_mail_setting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
