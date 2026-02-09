from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def coaches_dashboard(request: HttpRequest) -> HttpResponse:
    return render(request, 'coaches/coaches-dashboard.html')


def coach_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'coaches/coach-add.html')


def coach_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'coaches/coach-edit.html')


def coach_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'coaches/coach-delete.html')