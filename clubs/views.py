from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def clubs_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'clubs/clubs_dashboard.html')


def club_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'clubs/club_add.html')


def club_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'clubs/club_edit.html')


def club_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'clubs/club_delete.html')