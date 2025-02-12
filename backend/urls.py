from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'tournaments', views.TournamentsViewSet, basename='tournaments')

# список url маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
	path('api/v1/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
