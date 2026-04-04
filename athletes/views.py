from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
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
    paginate_by = 6


class AthleteDetailsView(DetailView):
    model = Athlete
    template_name = 'athletes/athlete-details.html'


class AthleteAddView(PermissionRequiredMixin, AthletesBaseViewMixin, CreateView):
    permission_required = 'athletes.add_athlete'
    form_class = AthleteAddForm
    template_name = 'athletes/athlete-add.html'


class AthleteEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'athletes.change_athlete'
    model = Athlete
    form_class = AthleteEditForm
    template_name = 'athletes/athlete-edit.html'

    def get_success_url(self):
        return reverse(
            'athletes:details',
            kwargs={
                'pk': self.object.pk
            }
        )


class AthleteDeleteView(PermissionRequiredMixin, AthletesBaseViewMixin, DeleteView):
    permission_required = 'athletes.delete_athlete'
    form_class = AthleteDeleteForm
    template_name = 'athletes/athlete-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
