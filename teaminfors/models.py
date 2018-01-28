from django.db import models

# Create your models here.

class LeagueTable(models.Model):
    position
    team_name
    matches_played
    lost
    drawn
    won
    goals_for
    goals_against

class Team(models.Model):
    name 
    city
    address
    established_date

class News(models.Model):
    news_id
    teams_ tagged
    date_issued
    read_content
    