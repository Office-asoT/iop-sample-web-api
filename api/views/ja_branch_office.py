from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import JaBranchOffice
from api.serializers import JaBranchOfficePublicSerializer

class JaBranchOfficeList(APIView):

    def get(self, request):
        jaBranchOffices = JaBranchOffice.objects.all()
        serializer = JaBranchOfficePublicSerializer(jaBranchOffices, many=True)
        return Response(serializer.data)
