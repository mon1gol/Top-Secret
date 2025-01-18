from rest_framework import serializers
from main.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tournament
        fields = "__all__"