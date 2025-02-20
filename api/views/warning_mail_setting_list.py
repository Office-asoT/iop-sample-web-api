from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import WarningMailSetting
from api.serializers import WarningMailSettingPublicSerializer, WarningMailSettingCreateSerializer

class WarningMailSettingList(APIView):

    def get(self, request, user_id):
        warning_mail_settings = WarningMailSetting.objects.filter(user_id=user_id).all()
        serializer = WarningMailSettingPublicSerializer(warning_mail_settings, many=True)
        respons_data = serializer.data
        return Response(respons_data)

    def post(self, request, user_id):
        data = request.data.copy()
        data['user_id'] = user_id
        serializer = WarningMailSettingCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
