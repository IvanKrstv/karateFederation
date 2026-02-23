from django.contrib import admin
from athletes.models import Athlete, Team

# Register your models here.

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'belt', 'gender', 'birth_date')
    list_filter = ('club', 'belt', 'gender')
    search_fields = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'club')
    list_filter = ('club',)
    search_fields = ('name',)
