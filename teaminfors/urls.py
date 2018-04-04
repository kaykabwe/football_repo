from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('club/', views.details, name='football-club'),
    #path('league-news/', views.newscorner, name='news')
]