from rest_framework import serializers

from .models import CategoryTournament, Tournament


class TournamentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tournament
        fields = "__all__"