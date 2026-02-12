from django.urls import path, include
from clubs import views

app_name = 'clubs'

clubs_actions_urls = [
    path('details/', views.ClubDetailView.as_view(), name='details'),
    path('edit/', views.ClubEditView.as_view(), name='edit'),
    path('delete/', views.ClubDeleteView.as_view(), name='delete')
]

urlpatterns = [
    path('', views.ClubsDashboardView.as_view(), name='dashboard'),
    path('add/', views.ClubAddView.as_view(), name='add'),
    path('<int:pk>/', include(clubs_actions_urls))
]


