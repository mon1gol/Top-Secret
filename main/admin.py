from django.contrib import admin
from main.models import Tournament, TournamentRules, TournamentAssessment, Team


admin.site.register(Tournament)
admin.site.register(TournamentRules)
admin.site.register(TournamentAssessment)
admin.site.register(Team)