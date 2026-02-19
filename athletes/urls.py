from django.urls import path, include
from athletes import views

app_name = 'athletes'

urlpatterns = [
    path('', views.AthletesDashboardView.as_view(), name='dashboard'),
    path('add/', views.AthleteAddView.as_view(), name='add'),
    path('<int:pk>', include([
        path('details/', views.AthleteDetailsView.as_view(), name='details'),
        path('edit/', views.AthleteEditView.as_view(), name='edit'),
        path('delete/', views.AthleteDeleteView.as_view(), name='delete')
    ]))

]