from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from athletes.forms import AthleteAddForm, AthleteEditForm, AthleteDeleteForm
from athletes.models import Athlete


# Create your views here.
class AthletesBaseViewMixin:
    model = Athlete
    success_url = reverse_lazy('athletes:dashboard')


class AthletesDashboardView(ListView):
    model = Athlete
    template_name = 'athletes/athletes-dashboard.html'
    context_object_name = 'athletes'


class AthleteDetailsView(DetailView):
    model = Athlete
    template_name = 'athletes/athlete-details.html'


class AthleteAddView(AthletesBaseViewMixin, CreateView):
    form_class = AthleteAddForm
    template_name = 'athletes/athlete-add.html'


class AthleteEditView(AthletesBaseViewMixin, UpdateView):
    form_class = AthleteEditForm
    template_name = 'athletes/athlete-edit.html'


class AthleteDeleteView(AthletesBaseViewMixin, DeleteView):
    form_class = AthleteDeleteForm
    template_name = 'athletes/athlete-delete.html'
