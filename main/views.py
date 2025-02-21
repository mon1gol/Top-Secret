from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tournament
from .serializers import TournamentSerializer


class LatestTournamentsList(APIView):
    def get(self, request, format=None):
        tournaments = Tournament.objects.all()[0:4]
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)
    
class TournamentDetail(APIView):
    def get_object(self, category_slug, tournament_slug):
        try:
            return Tournament.objects.filter(category__slug=category_slug).get(slug=tournament_slug)
        except Tournament.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, tournament_slug, format=None):
        tournament = self.get_object(category_slug, tournament_slug)
        serializer = TournamentSerializer(tournament)
        return Response(serializer.data)