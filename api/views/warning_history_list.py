from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import WarningHistory
from api.serializers import WarningHistoryPublicSerializer

class WarningHistoryList(APIView):

    def get(self, request, user_id):
        warning_histories = WarningHistory.objects.filter(user_id=user_id).all()
        serializer = WarningHistoryPublicSerializer(warning_histories, many=True)
        respons_data = serializer.data
        return Response(respons_data)
