from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from api.models import DeliveryEmailAddress
from api.serializers import DeliveryEmailAddressPublicSerializer, DeliveryEmailAddressCreateSerializer, DeliveryEmailAddressUpdateSerializer

class DeliveryEmailAddressDetail(APIView):

    def get(self, request, user_id):
        respons_data = [];
        delivery_eamil_addless = DeliveryEmailAddress.objects.filter(user_id=user_id).order_by('id')

        if delivery_eamil_addless:
            serializer = DeliveryEmailAddressPublicSerializer(delivery_eamil_addless, many=True)
            respons_data = serializer.data

        return Response(respons_data)

    def put(self, request, user_id):
        if not isinstance(request.data, list):
            return Response({"error": "Invalid data format, expected a list"}, status=status.HTTP_400_BAD_REQUEST)

        all_data = []
        for data_chunk in request.data:
            data_chunk['user_id'] = user_id

            # 既存データを取得
            existing_instance = DeliveryEmailAddress.objects.filter(
                user_id=data_chunk['user_id'],
                email_address=data_chunk['email_address']
            ).first()

            if existing_instance:
                # 既存データがある場合は `UpdateSerializer` を使う
                serializer = DeliveryEmailAddressUpdateSerializer(existing_instance, data=data_chunk, partial=True)
            else:
                # 新規データなら `CreateSerializer` を使う
                serializer = DeliveryEmailAddressCreateSerializer(data=data_chunk)

            if serializer.is_valid():
                serializer.save()
                all_data.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(all_data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, user_id):
        delivery_email_address = DeliveryEmailAddress.objects.filter(user_id=user_id, email_address=request.data['email_address']).first()

        if not delivery_email_address:
            raise Http404
        delivery_email_address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    