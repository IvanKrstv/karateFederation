from django.urls import path, include
from tournaments import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.TournamentsDashboardView.as_view(), name='dashboard'),
    path('add/', views.TournamentAddView.as_view(), name='add'),
    path('<int:pk>/', include([
        path('details/', views.TournamentDetailView.as_view(), name='details'),
        path('edit/', views.TournamentEditView.as_view(), name='edit'),
        path('delete/', views.TournamentDeleteView.as_view(), name='delete')
    ]))
]