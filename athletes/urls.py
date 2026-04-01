from django.urls import path, include
from athletes import views, api_views

app_name = 'athletes'

api_urls = [
    path('', api_views.AthletesListApiView.as_view(), name='api-list'),
    path('<int:pk>/', api_views.AthleteDetailApiView.as_view(), name='api-details')
]

urlpatterns = [
    path('', views.AthletesDashboardView.as_view(), name='dashboard'),
    path('add/', views.AthleteAddView.as_view(), name='add'),

    path('<int:pk>/', include([
        path('details/', views.AthleteDetailsView.as_view(), name='details'),
        path('edit/', views.AthleteEditView.as_view(), name='edit'),
        path('delete/', views.AthleteDeleteView.as_view(), name='delete')
    ])),

    # API urls
    path('api/', include(api_urls)),
]