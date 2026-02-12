from django.urls import path
from django.views.generic import TemplateView

from common import views

app_name = 'common'

urlpatterns = [
    path('', TemplateView.as_view(template_name='common/home-page.html'), name='home'),
]