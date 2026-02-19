from django.urls import path, include
from coaches import views

app_name = 'coaches'

urlpatterns = [
    path('', views.CoachesDashboardView.as_view(), name='dashboard'),
    path('add/', views.CoachAddView.as_view(), name='add'),
    path('<int:pk>/', include([
        path('details/', views.CoachDetailView.as_view(), name='details'),
        path('edit/', views.CoachEditView.as_view(), name='edit'),
        path('delete/', views.CoachDeleteView.as_view(), name='delete')
    ]))
]