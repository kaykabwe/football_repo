from django.db import models

# Create your models here.

class LeagueTable(models.Model):
    position = models.IntegerField()
    # team_name = models.CharField(max_length=80)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches_played = models.IntegerField(null=False)    # null is false by default
    lost = models.IntegerField(null=False)
    drawn = models.IntegerField(null=False)
    won = models.IntegerField(null=False)
    goals_for = models.IntegerField(null=False)
    goals_against = models.IntegerField(null=False)

    # to show readable string of class 
    def __str__(self):
        return "This is the league table"

class Team(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    est_date = models.DateTimeField('established date')

    def __str__(self):
        return self.name

class News(models.Model):
    news_id = models.IntegerField()
    # teams_tagged = models.CharField(max_length=80)
    team_tagged = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_issued = est_date = models.DateTimeField('Date\
     news article is published')
    read_content = models.TextField()
    
    def __str__(self):
        return self.news_id
