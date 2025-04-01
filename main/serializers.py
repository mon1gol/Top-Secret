from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class TournamentRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRules
        fields = (
            "min_members_in_team",
            "max_members_in_team",
            "date_start",
            "date_end",
            "id_tournament",
        )

class TournamentSerializer(serializers.ModelSerializer):
    rules = TournamentRulesSerializer(source="tournamentrules", read_only=True)
    class Meta:
        model = Tournament
        fields = (
            "id",
            "get_absolute_url",
            "get_image",
            "name",
            "description",
            "rules",
        )

class CategorySerializer(serializers.ModelSerializer):
    tournaments = TournamentSerializer(many=True)
    class Meta:
        model = CategoryTournament
        fields = (
            "id",
            "get_absolute_url",
            "name",
            "slug",
            "tournaments",
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )

class TeamSerializer(serializers.ModelSerializer):
    usernames = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'description',
            'logo',
            'get_image',
            'id_tournament',
            'usernames',
        )
        extra_kwargs = {
            'logo': {'required': False},
            'description': {'required': False},
        }

class TeamProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProject
        fields = (
            'id',
            'team',
            'tournament',
            'description',
            'file_name',
            'get_file_project',
        )
        extra_kwargs = {
            'file_name': {'required': False}
        }

class AssessmentSerializer(serializers.ModelSerializer):
    criterion = serializers.CharField(source='criterion.name')
    max_score = serializers.IntegerField(source='criterion.max_score')
    class Meta:
        model = TeamAssessment
        fields = (
            'criterion', 
            'score', 
            'max_score'
        )

class TeamSerializer(serializers.ModelSerializer):
    tournament = serializers.CharField(source='id_tournament.name')
    assessments = AssessmentSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = (
            'id', 
            'name', 
            'tournament',
            'assessments'
        )
    def get_assessments(self, obj):
        filtered_assessments = getattr(obj, 'filtered_assessments', obj.assessments.all())
        return AssessmentSerializer(filtered_assessments, many=True).data
    

class TeamCreateSerializer(serializers.ModelSerializer):
    usernames = serializers.ListField(
        child=serializers.CharField(max_length=150),
        write_only=True
    )
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'id_tournament',
            'usernames',
        )