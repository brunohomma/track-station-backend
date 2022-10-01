from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from track_station.settings import WHERETHEISS_API, ISS_ID
from track.serializers import TrackSerializer

import requests

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['POST'])
    def track(self, request):
        endpoint = f"/satellites/{ISS_ID}"
        response = requests.get(WHERETHEISS_API+endpoint)
        serializer = TrackSerializer(data=response.json())
        try:
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'some error has occurred'}, status=status.HTTP_400_BAD_REQUEST)
