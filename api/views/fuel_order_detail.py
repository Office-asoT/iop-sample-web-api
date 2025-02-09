from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from api.models import FuelOrder
from api.serializers import FuelOrderCreateSerializer, FuelOrderStatusUpdateSerializer

class FuelOrderDetail(APIView):

    def post(self, request, user_id, *args, **kwargs):
        data = request.data.copy()
        data['user_id'] = user_id
        serializer = FuelOrderCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data.pop('id', None)  # id をレスポンスから除外
            print("Response Data:", response_data) 
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id, *args, **kwargs):
        serializer = FuelOrderStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            order_date = serializer.validated_data['order_date']
            status_value = serializer.validated_data['status']

            # user_id と order_date で検索
            instance = get_object_or_404(FuelOrder, user_id=user_id, order_date=order_date)
            instance.status = status_value
            instance.save()

            return Response({"status": instance.status}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
