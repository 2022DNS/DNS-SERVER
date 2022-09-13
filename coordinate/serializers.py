from rest_framework import serializers
from .models import Road



class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = (
            'id',
            'longitude',
            'latitude',
            'count',
            'date'
        )

class RoadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = (
            'longitude',
            'latitude',
            'count'
        )