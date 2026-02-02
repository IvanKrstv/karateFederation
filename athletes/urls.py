from django.urls import path
from athletes import views

app_name = 'athletes'

urlpatterns = [
    path('', views.athletes_dashboard, name='dashboard')
]