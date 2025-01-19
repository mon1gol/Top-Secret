from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'tournaments', views.TournamentsViewSet, basename='tournaments')

# список url маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/tournaments/
]
