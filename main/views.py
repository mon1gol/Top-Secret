from django.http import HttpResponse
from rest_framework import generics
from main.models import Tournament
from main.serializers import TournamentSerializer
from main.models import *


class TournamentsAPIList(generics.ListCreateAPIView):    
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


def index(request):
    return HttpResponse('Home page')
