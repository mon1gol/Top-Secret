from django.contrib import admin
from main.models import CategoryTournament, Tournament, TournamentRules, TournamentAssessment, Team


admin.site.register(CategoryTournament)
admin.site.register(Tournament)
admin.site.register(TournamentRules)
admin.site.register(TournamentAssessment)
admin.site.register(Team)