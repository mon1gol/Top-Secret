from rest_framework import serializers

from .models import CategoryTournament, Tournament


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