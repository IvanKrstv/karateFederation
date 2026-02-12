from django.urls import path, include
from athletes import views

app_name = 'athletes'

urlpatterns = [
    path('', views.athletes_dashboard, name='dashboard'),
    path('add/', views.athlete_add, name='add'),
    path('edit/', views.athlete_edit, name='edit'),
    path('delete/', views.athlete_delete, name='delete')
]