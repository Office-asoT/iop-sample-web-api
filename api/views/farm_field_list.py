from rest_framework.views import APIView
from rest_framework.response import Response

class FarmFieldList(APIView):

    def get(self, request, user_id):
        farm_field_list = [
            {
                'id': 'farm-field-a',
                'name': '圃場A',
                'address': '〒780-8571 高知県高知市本町５丁目１−４５',
                'latitude': 33.559706,
                'longitude': 133.531081,
                'crop': 'トマト',
                'plantingDate': '2024-10-01',
                'extensionOffice': '高知中央普及所',
                'jaFuelSupplier': 'JA高知中央',
            },
            {
                'id': 'farm-field-b',
                'name': '圃場B',
                'address': '〒783-8501 高知県南国市大そね乙６２５−１',
                'latitude': 33.575178,
                'longitude': 133.641388,
                'crop': 'ナス',
                'plantingDate': '2024-09-01',
                'extensionOffice': '南国普及所',
                'jaFuelSupplier': 'JA南国',
            },
            {
                'id': 'farm-field-c',
                'name': '圃場C',
                'address': '〒781-5292 高知県香南市野市町西野2706番地',
                'latitude': 33.564227,
                'longitude': 133.700758,
                'crop': 'ピーマン',
                'plantingDate': '2024-08-15',
                'extensionOffice': '中央東農業振興センター',
                'jaFuelSupplier': 'JA野市支所',
            },
        ]

        return Response(farm_field_list)
