from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tournament
from .serializers import TournamentSerializer


class LatestTournamentsList(APIView):
    def get(self, request, format=None):
        tournaments = Tournament.objects.all()[0:4]
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)