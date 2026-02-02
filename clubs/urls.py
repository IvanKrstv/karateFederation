from django.urls import path, include
from clubs import views

app_name = 'clubs'

clubs_actions_urls = [
    path('edit/', views.club_edit, name='edit'),
    path('delete/', views.club_delete, name='delete')
]

urlpatterns = [
    path('', views.clubs_dashboard, name='dashboard'),
    path('add/', views.club_add, name='add'),
    path('<int:pk>/', include(clubs_actions_urls))
]


