from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path ('admin/',admin.site.urls),
    path ('MovieAnime_list/', views.MovieAnime_list, name='MovieAnime_list'),
]