from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from tournaments.forms import TournamentDeleteForm, TournamentEditForm, TournamentAddForm
from tournaments.models import Tournament


# Create your views here.
class TournamentBaseViewMixin:
    model = Tournament
    success_url = reverse_lazy('tournaments:dashboard')


class TournamentsDashboardView(ListView):
    model = Tournament
    template_name = 'tournaments/tournaments-dashboard.html'
    context_object_name = 'tournaments'
    paginate_by = 6


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournaments/tournament-details.html'


class TournamentAddView(TournamentBaseViewMixin, CreateView):
    form_class = TournamentAddForm
    template_name = 'tournaments/tournament-add.html'


class TournamentEditView(UpdateView):
    model = Tournament
    form_class = TournamentEditForm
    template_name = 'tournaments/tournament-edit.html'

    def get_success_url(self):
        return reverse(
            'tournaments:details',
            kwargs={
                'pk': self.object.pk
            }
        )


class TournamentDeleteView(TournamentBaseViewMixin, DeleteView):
    form_class = TournamentDeleteForm
    template_name = 'tournaments/tournament-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
