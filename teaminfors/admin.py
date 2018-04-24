from django.contrib import admin
from .models import Team, LeagueTable

# Register your models here.
admin.site.register(Team)

admin.site.register(LeagueTable)