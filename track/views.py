from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from helpers.communications import WhereTheISSAPI
from track.serializers import TrackSerializer

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['POST', 'GET'])
    def track(self, request):
        satellite_id = WhereTheISSAPI.get_satellite_id("/satellites", name="iss")
        data = WhereTheISSAPI.get_iss_data_treated(f"/satellites/{satellite_id}")
        serializer = TrackSerializer(data=data)
        try:
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'some error has occurred'}, status=status.HTTP_400_BAD_REQUEST)
