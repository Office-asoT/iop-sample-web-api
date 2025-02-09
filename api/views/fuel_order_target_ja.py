from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import FuelOrderTargetJa
from api.serializers import FuelOrderTargetJaPublicSerializer, FuelOrderTargetJaUpdateSerializer

class FuelOrderTargetJaDetail(APIView):

    def get(self, request, user_id):
        respons_data = [];
        fuel_order_targets = FuelOrderTargetJa.objects.filter(user_id=user_id).order_by('id')

        if fuel_order_targets:
            serializer = FuelOrderTargetJaPublicSerializer(fuel_order_targets, many=True)
            respons_data = serializer.data

        return Response(respons_data)
    
    def patch(self, request, user_id):
        if not isinstance(request.data, list):
            return Response({"error": "Invalid data format, expected a list"}, status=status.HTTP_400_BAD_REQUEST)
        
        all_data = []
        for data_chunk in request.data:
            data_chunk['user_id'] = user_id
            existing_instance = FuelOrderTargetJa.objects.filter(
                user_id=data_chunk['user_id'],
                farm_field_id=data_chunk['farm_field_id']
            ).first()
            serializer = FuelOrderTargetJaUpdateSerializer(existing_instance, data=data_chunk, partial=True)
            if serializer.is_valid():
                hoge = serializer.save()
                all_data.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(all_data, status=status.HTTP_200_OK)
