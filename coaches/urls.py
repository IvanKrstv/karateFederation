from django.urls import path, include
from coaches import views

app_name = 'coaches'

urlpatterns = [
    path('', views.coaches_dashboard, name='dashboard'),
    path('<slug:club_slug>/coach/', include([
        path('add/', views.coach_add, name='add'),
        path('edit/', views.coach_edit, name='edit'),
        path('delete/', views.coach_delete, name='delete')
    ]))

]