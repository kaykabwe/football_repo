from django.db import models

# Create your models here.

class LeagueTable(models.Model):
    position
    team_name = models.CharField(max_length=60)
    matches_played = models.IntegerField
    lost = models.IntegerField
    drawn = models.IntegerField
    won = models.IntegerField
    goals_for = models.IntegerField
    goals_against = models.IntegerField

    # to show readable string of class 
    def __str__(self):
        return self.question_text

class Team(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    est_date = models.DateTimeField('established date')

    def __str__(self):
        return self.question_text

class News(models.Model):
    news_id = models.IntegerField
    teams_tagged = models.CharField(max_length=60)
    date_issued = est_date = models.DateTimeField('Date\
     news article is published')
    read_content = models.TextField
    
    def __str__(self):
        return self.question_text