from rest_framework import serializers

from api.models import Municipality

class MunicipalityPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = [
            'code',
            'name',
            'latitude',
            'longitude',
            'zipcode',
            'address',
        ]
