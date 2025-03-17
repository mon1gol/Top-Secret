from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            "id",
            "get_absolute_url",
            "get_image",
            "name",
            "description"
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