from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def athletes_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'athletes/athletes-dashboard.html')


def athlete_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'athletes/athlete-add.html')


def athlete_edit(request: HttpRequest) -> HttpResponse:
    return render(request, 'athletes/athlete-edit.html')


def athlete_delete(request: HttpRequest) -> HttpResponse:
    return render(request, 'athletes/athlete-delete.html')