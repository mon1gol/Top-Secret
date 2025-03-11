from django.http import Http404
from rest_framework import status
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import *
from .serializers import *


class LatestTournamentsList(APIView):
    def get(self, request, format=None):
        tournaments = Tournament.objects.all()
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
    
class TournamentsByStatus(APIView):
    def get(self, request, status_slug, format=None):
        today = datetime.today().date()
        if status_slug == 'upcoming':
            tournaments = Tournament.objects.filter(tournamentrules__date_start__gt=today)
        elif status_slug == 'comingnow':
            tournaments = Tournament.objects.filter(
                tournamentrules__date_start__lte=today,
                tournamentrules__date_start__gte=today
            )
        elif status_slug == 'completed':
            tournaments = Tournament.objects.filter(tournamentrules__date_start__lt=today)
        else:
            return Response({"error": "Неверный статус"}, status=400)
        
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return CategoryTournament.objects.get(slug=category_slug)
        except Tournament.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class UsersList(APIView):
    def get(self, request, format=None):
        usernames = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(usernames, many=True)
        return Response(serializer.data)

class TeamActions(APIView):
    def get_object(self, tournament_slug):
        try:
            return Tournament.objects.get(slug=tournament_slug)
        except Tournament.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, tournament_slug, format=None):
        tournament = self.get_object(tournament_slug)
        teams = Team.objects.filter(id_tournament=tournament)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, category_slug, tournament_slug, format=None):
        serializer = TeamSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        validated_data = serializer.validated_data   
        usernames = validated_data.pop('usernames', [])

        tournament = self.get_object(tournament_slug)
        teams_in_tournament = Team.objects.filter(id_tournament=tournament)

        existing_members = LinkToTeamMember.objects.filter(
            user__username__in=usernames,
            team__in=teams_in_tournament
        ).values_list('user__username', flat=True).distinct()

        if existing_members.exists():
            error_users = list(existing_members)
            return Response(
                {
                    "error": f"Пользователи {error_users} уже участвуют в других командах этого турнира."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
        team = Team.objects.create(**validated_data)
        users = User.objects.filter(username__in=usernames)
        
        for user in users:
            LinkToTeamMember.objects.create(user=user, team=team)

        return Response(
            {
                "message": "Команда успешно создана.",
                "team_name": team.name,
                "members": list(usernames)
            },
            status=status.HTTP_201_CREATED
        )