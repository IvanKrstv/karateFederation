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


class AthleteDetailsView(DetailView):
    model = Athlete
    template_name = 'athletes/athlete-details.html'


class AthleteAddView(AthletesBaseViewMixin, CreateView):
    form_class = AthleteAddForm
    template_name = 'athletes/athlete-add.html'


class AthleteEditView(UpdateView):
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


class AthleteDeleteView(AthletesBaseViewMixin, DeleteView):
    form_class = AthleteDeleteForm
    template_name = 'athletes/athlete-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
