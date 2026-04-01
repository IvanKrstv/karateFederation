from django.contrib import admin

from tournaments.models import Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'country', 'city')
    list_filter = ('country',)
    search_fields = ('name', 'city', 'country')
