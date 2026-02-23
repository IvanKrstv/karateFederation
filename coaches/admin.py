from django.contrib import admin
from coaches.models import Coach

# Register your models here.

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'coach_license', 'gender', 'birth_date')
    list_filter = ('club', 'coach_license', 'gender')
    search_fields = ('name',)