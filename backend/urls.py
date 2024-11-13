from django.contrib import admin
from django.urls import path

from main import views


# список url маршрутов
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
