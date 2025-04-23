from django import forms
from django.contrib import admin
from main.models import *


admin.site.register(Team)
admin.site.register(TeamProject)
admin.site.register(Tournament)
admin.site.register(TournamentRules)
admin.site.register(CategoryTournament)
admin.site.register(LinkToTeamMember)
admin.site.register(Criterion)
admin.site.register(TournamentCriterion)
admin.site.register(TeamAssessment)
