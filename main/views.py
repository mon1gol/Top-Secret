from requests import Response
from rest_framework import generics
from rest_framework.views import APIView
from main.models import Hackathon
from main.serializers import HackathonSerializer


class TournamentsAPIList(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    