from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from coaches.forms import CoachAddForm, CoachEditForm, CoachDeleteForm
from coaches.models import Coach


# Create your views here.
class CoachBaseViewMixin:
    model = Coach
    success_url = reverse_lazy('coaches:dashboard')


class CoachesDashboardView(ListView):
    model = Coach
    template_name = 'coaches/coaches-dashboard.html'
    context_object_name = 'coaches'


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coaches/coach-details.html'


class CoachAddView(CoachBaseViewMixin, CreateView):
    form_class = CoachAddForm
    template_name = 'coaches/coach-add.html'


class CoachEditView(CoachBaseViewMixin, UpdateView):
    form_class = CoachEditForm
    template_name = 'coaches/coach-edit.html'


class CoachDeleteView(CoachBaseViewMixin, DeleteView):
    form_class = CoachDeleteForm
    template_name = 'coaches/coach-delete.html'
