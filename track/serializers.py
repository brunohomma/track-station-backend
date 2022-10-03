from rest_framework import serializers

class TrackSerializer(serializers.Serializer):
    latitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    longitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    altitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)