from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from clubs.forms import ClubAddForm, ClubEditForm, ClubDeleteForm
from clubs.models import Club


# Create your views here.
class ClubsDashboardView(ListView):
    model = Club
    template_name = 'clubs/clubs-dashboard.html'
    context_object_name = 'clubs'


class ClubDetailView(DetailView):
    model = Club
    template_name = 'clubs/club-details.html'


class ClubAddView(CreateView):
    model = Club
    form_class = ClubAddForm
    template_name = 'clubs/club-add.html'
    success_url = reverse_lazy('clubs:dashboard')


class ClubEditView(UpdateView):
    model = Club
    form_class = ClubEditForm
    template_name = 'clubs/club-edit.html'
    success_url = reverse_lazy('clubs:dashboard')


class ClubDeleteView(DeleteView):
    model = Club
    form_class = ClubDeleteForm
    template_name = 'clubs/club-delete.html'
    success_url = reverse_lazy('clubs:dashboard')
