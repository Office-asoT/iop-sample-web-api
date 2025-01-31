from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Municipality
from api.serializers import MunicipalityPublicSerializer

class MunicipalityList(APIView):

    def get(self, request):
        municipalities = Municipality.objects.all()
        serializer = MunicipalityPublicSerializer(municipalities, many=True)
        return Response(serializer.data)
