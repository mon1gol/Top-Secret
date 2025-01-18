from rest_framework import serializers
from main.models import Hackathon


class HackathonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hackathon
        fields = "__all__"