from django.contrib import admin

from accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ('username',)