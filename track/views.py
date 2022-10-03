from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from helpers.communications import WhereTheISSAPI, TLEAPI
from track.serializers import TrackSerializer
from service.redis_service import redis_client, DAY_TIME
from helpers.calculations import get_satellite_geo_position

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['POST', 'GET'])
    def track_by_where_the_iss_at(self, request):
        satellite_id = WhereTheISSAPI.get_satellite_id("/satellites", name="iss")
        data = WhereTheISSAPI.get_iss_data_treated(f"/satellites/{satellite_id}")
        serializer = TrackSerializer(data=data)
        try:
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'some error has occurred'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST', 'GET'])
    def track_by_tle_api(self, request):
        if redis_client._exist_key('tle_1') and redis_client._exist_key('tle_2'):
            data = TLEAPI.get_satellite_info("/api/tle/")
            line_1 = data.get('line1')
            line_2 = data.get('line2')
            redis_client._set_value_by_key_redis('tle_1', line_1, expire_key=True, expire_time=DAY_TIME)
            redis_client._set_value_by_key_redis('tle_2', line_2, expire_key=True, expire_time=DAY_TIME)
        else:
            line_1 = redis_client._get_value_by_key_redis('tle_1')
            line_2 = redis_client._get_value_by_key_redis('tle_2')
        
        try:
            lat, lon, height = get_satellite_geo_position(line_1, line_2)

            data = {
                'latitude': lat,
                'longitude': lon,
                'altitude': height
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'some error has occurred'}, status=status.HTTP_400_BAD_REQUEST)
