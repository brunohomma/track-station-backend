from rest_framework import serializers

class TrackSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=216)
    id = serializers.IntegerField(required=True)
    latitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    longitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    altitude = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    velocity = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    visibility = serializers.CharField(required=True, max_length=216)
    footprint = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    timestamp = serializers.IntegerField(required=True)
    daynum = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    solar_lat = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    solar_lon = serializers.DecimalField(required=True,max_digits=None, decimal_places=12)
    units = serializers.CharField(required=True, max_length=216)