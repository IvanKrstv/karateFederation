from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def coaches_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'coaches/coaches_dashboard')