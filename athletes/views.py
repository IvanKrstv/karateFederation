from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def athletes_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'athletes/athletes_dashboard')