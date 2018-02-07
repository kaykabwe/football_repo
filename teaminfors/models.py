from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    city = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField()
    est_date = models.DateTimeField('established date')

    def __str__(self):
        description = "{0}, {1}, email as {2}, {3}, {4}".format(self.name, 
            self.city, self.email, self.address, self.est_date)
        return description

class LeagueTable(models.Model):
    position = models.IntegerField(db_index=True)
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches_played = models.IntegerField(null=False, default=0)    # null is false by default
    lost = models.IntegerField(null=False, default=0)
    drawn = models.IntegerField(null=False, default=0)
    won = models.IntegerField(null=False, default=0)
    goals_for = models.IntegerField(null=False, default=0)
    goals_against = models.IntegerField(null=False, default=0)

    # to show readable string of class 
    def __str__(self):
        return "This is the league table"

class News(models.Model):
    news_id = models.IntegerField(unique=True)
    team_tagged = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_issued = models.DateTimeField('Date\
     news article is published')
    read_content = models.TextField()
    
    def __str__(self):
        return self.news_id

    def date_published(self):
        return (self.date_issued)