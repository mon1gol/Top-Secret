from requests import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from main.models import Tournament
from main.serializers import TournamentSerializer
from main.models import *


class TournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    @action(methods=['get'], detail=False)
    def getname(self, request):
        tournaments = Tournament.objects.all()
        return Response({'name': [t.name for t in tournaments]})
    