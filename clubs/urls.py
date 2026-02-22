from django.urls import path, include
from clubs import views

app_name = 'clubs'

teams_actions_urls = [
    path('add/', views.TeamAddView.as_view() , name='team-add'),
    path('<int:team_pk>/', include([
        path('edit/', views.TeamEditView.as_view(), name='team-edit'),
        path('delete/', views.TeamDeleteView.as_view(), name='team-delete')
    ]))
]

clubs_actions_urls = [
    path('details/', views.ClubDetailView.as_view(), name='details'),
    path('edit/', views.ClubEditView.as_view(), name='edit'),
    path('delete/', views.ClubDeleteView.as_view(), name='delete'),
    path('teams/', include(teams_actions_urls))
]

urlpatterns = [
    path('', views.ClubsDashboardView.as_view(), name='dashboard'),
    path('add/', views.ClubAddView.as_view(), name='add'),
    path('<int:pk>/', include(clubs_actions_urls))
]


