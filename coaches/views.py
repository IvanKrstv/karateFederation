from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
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
    paginate_by = 6


class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coaches/coach-details.html'


class CoachAddView(PermissionRequiredMixin, CoachBaseViewMixin, CreateView):
    permission_required = 'coaches.add_coach'
    form_class = CoachAddForm
    template_name = 'coaches/coach-add.html'


class CoachEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'coaches.change_coach'
    model = Coach
    form_class = CoachEditForm
    template_name = 'coaches/coach-edit.html'

    def get_success_url(self):
        return reverse(
            'coaches:details',
            kwargs={
                'pk': self.object.pk
            }
        )


class CoachDeleteView(PermissionRequiredMixin, CoachBaseViewMixin, DeleteView):
    permission_required = 'coaches.delete_coach'
    form_class = CoachDeleteForm
    template_name = 'coaches/coach-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
