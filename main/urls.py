from django.urls import path, include

from main import views


urlpatterns = [
    path('latest-tournaments/', views.LatestTournamentsList.as_view()),
    path('tournaments/<slug:category_slug>/<slug:tournament_slug>/', views.TournamentDetail.as_view()),
    path('tournaments/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('users-list/', views.UsersList.as_view()),
]
