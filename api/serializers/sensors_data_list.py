from rest_framework import serializers

class SensorsDataListGetSerializer(serializers.Serializer):
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
