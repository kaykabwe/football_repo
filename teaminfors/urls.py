from django.urls import path

from . import views

app_name = 'teaminfors' # namespacing a url

urlpatterns = [
    path('', views.index, name='index'),
    path('your_name/', views.get_name, name='your_name'),
    path('your_name/thanks/', views.newscorner, name='thanks'),
    #path('club/', views.details, name='football-club'),
    #path('league-news/', views.newscorner, name='news')
]