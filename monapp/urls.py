from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accueil/', views.accueil_list, name='accueil_list'),
    path('missions/', views.mission_list, name='mission_list'),
    path('drones/', views.drone_list, name='drone_list'),
    path('stations/', views.station_list, name='station_list'),
    path('donnees/', views.donnees_list, name='donnees_list'),
    path('messages/', views.message_list, name='message_list'),
]