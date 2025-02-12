from django.urls import path, include

from main import views


urlpatterns = [
    path('latest-tournaments/', views.LatestTournamentsList.as_view()),
]
