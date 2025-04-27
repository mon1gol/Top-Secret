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
                tournamentrules__date_end__gte=today
            )
        elif status_slug == 'completed':
            tournaments = Tournament.objects.filter(tournamentrules__date_end__lt=today)
        else:
            return Response({"error": "Неверный статус"}, status=400)
        
        serializer = TournamentSerializer(tournaments, many=True)
        return Response(serializer.data)
    
class TournamentsByStatusByUser(APIView):
    def get(self, request, status_slug, username_slug, format=None):
        today = datetime.today().date()

        user = User.objects.get(username=username_slug)
        tournaments = Tournament.objects.filter(team__members__user=user).distinct()

        if status_slug == 'upcoming':
            tournaments_filtered = tournaments.filter(tournamentrules__date_start__gt=today)
        elif status_slug == 'comingnow':
            tournaments_filtered = tournaments.filter(
                tournamentrules__date_start__lte=today,
                tournamentrules__date_end__gte=today
            )
        elif status_slug == 'completed':
            tournaments_filtered = tournaments.filter(tournamentrules__date_end__lt=today)
        else:
            return Response({"error": "Неверный статус"}, status=400)
        
        serializer = TournamentSerializer(tournaments_filtered, many=True)
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
        serializer = TeamCreateSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, category_slug, tournament_slug, format=None):
        serializer = TeamCreateSerializer(data=request.data, context={'request': request})

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
            error_users = ", ".join(error_users)
            return Response(
                {
                    "error": f"Один или несколько пользователей - {error_users} уже участвуют в других командах этого турнира."
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
    
class TeamProjectView(APIView):
    def get(self, request, tournament_slug, username_slug, format=None):
        user = User.objects.get(username=username_slug)
        tournament = Tournament.objects.get(slug=tournament_slug)

        try:
            link_to_team_member = LinkToTeamMember.objects.get(user=user, team__id_tournament=tournament)
            team = link_to_team_member.team
        except LinkToTeamMember.DoesNotExist:
            return Response(
                {"error": "Пользователь не состоит в команде этого турнира."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        team_project = TeamProject.objects.filter(team=team)
        serializer = TeamProjectSerializer(team_project, many=True)
        return Response(serializer.data)
    
    def post(self, request, tournament_slug, username_slug, format=None):
        data = request.data
        tournament = Tournament.objects.get(slug=tournament_slug)
        user = User.objects.get(username=username_slug)

        try:
            link_to_team_member = LinkToTeamMember.objects.get(user=user, team__id_tournament=tournament)
            team = link_to_team_member.team
        except LinkToTeamMember.DoesNotExist:
            return Response(
                {"error": "Пользователь не состоит в команде этого турнира."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = request.data.copy()
        data['team'] = team.id
        data['tournament'] = tournament.id

        serializer = TeamProjectSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeamResults(APIView):
    def get(self, request, username_slug, format=None):
        try:
            user = User.objects.get(username=username_slug)
            user_team_links = user.team_memberships.all()
            user_teams = [link.team for link in user_team_links]

            for team in user_teams: 
                team.filtered_assessments = team.assessments.filter(tournament=team.id_tournament)

            serializer = TeamSerializer(user_teams, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)       
        except User.DoesNotExist:
            return Response(
                {'error': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
        
class TeamResultDetail(APIView):
    def get(self, request, username_slug, team_id, format=None):
        try:
            user = User.objects.get(username=username_slug)
            user_team_links = user.team_memberships.all()
            teams = [link.team for link in user_team_links if link.team.id == team_id]
            team = teams[0]
            
            team.filtered_assessments = team.assessments.filter(tournament=team.id_tournament)

            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)       
        except User.DoesNotExist:
            return Response(
                {'error': 'Пользователь не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
