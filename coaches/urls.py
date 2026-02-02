from django.urls import path
from coaches import views

app_name = 'coaches'

urlpatterns = [
    path('', views.coaches_dashboard, name='dashboard')
]