from django.contrib import admin
from django.urls import path
from main import views


# список url маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/index/', views.TournamentsAPIList.as_view()),
]
