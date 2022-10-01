from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from track_station.settings import WHERETHEISS_API, ISS_ID

import requests

# Create your views here.
class TrackViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['POST'])
    def track(self, request):
        endpoint = f"/satellites/{ISS_ID}"
        response = requests.get(WHERETHEISS_API+endpoint)
        return Response(response.json(), status=status.HTTP_200_OK)