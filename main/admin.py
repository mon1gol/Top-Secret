from django.contrib import admin
from main.models import Hackathon, HackathonRules, HackathonAssessment, Team


admin.site.register(Hackathon)
admin.site.register(HackathonRules)
admin.site.register(HackathonAssessment)
admin.site.register(Team)