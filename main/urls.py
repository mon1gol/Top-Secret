from django.urls import path, include

from main import views


urlpatterns = [
    path('users-list/', views.UsersList.as_view()), # users
    path('latest-tournaments/', views.LatestTournamentsList.as_view()),
    path('tournaments/<slug:category_slug>/', views.CategoryDetail.as_view()), # tournaments
    path('tournaments/status/<slug:status_slug>/', views.TournamentsByStatus.as_view()),
    path('tournaments/<slug:category_slug>/<slug:tournament_slug>/', views.TournamentDetail.as_view()),
    path('tournaments/status/<slug:status_slug>/<slug:username_slug>/', views.TournamentsByStatusByUser.as_view()),
    path('tournaments/<slug:category_slug>/<slug:tournament_slug>/teams/', views.TeamActions.as_view()), # teams
    path('projects/<slug:tournament_slug>/<slug:username_slug>/', views.TeamProjectView.as_view()),
]
