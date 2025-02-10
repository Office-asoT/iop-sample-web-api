from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import FuelOrder
from api.serializers import FuelOrderListPublicSerializer

class FuelOrderList(APIView):

    def get(self, request, user_id):
        respons_data = [];
        fuel_orders = FuelOrder.objects.filter(user_id=user_id).order_by('order_date').reverse()

        if fuel_orders:
            serializer = FuelOrderListPublicSerializer(fuel_orders, many=True)
            respons_data = serializer.data

        return Response(respons_data)
