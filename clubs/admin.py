from django.contrib import admin
from clubs.models import Club

# Register your models here.

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'founder_name', 'slug')
    prepopulated_fields = {'slug': ('name', 'city')}
    search_fields = ('name', 'city', 'founder_name')
