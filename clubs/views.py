from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from clubs.forms import ClubAddForm, ClubEditForm, ClubDeleteForm
from clubs.models import Club


# Create your views here.
class ClubsBaseViewMixin:
    model = Club
    success_url = reverse_lazy('clubs:dashboard')


class ClubsDashboardView(ListView):
    model = Club
    template_name = 'clubs/clubs-dashboard.html'
    context_object_name = 'clubs'


class ClubDetailView(DetailView):
    model = Club
    template_name = 'clubs/club-details.html'


class ClubAddView(ClubsBaseViewMixin, CreateView):
    form_class = ClubAddForm
    template_name = 'clubs/club-add.html'


class ClubEditView(ClubsBaseViewMixin, UpdateView):
    form_class = ClubEditForm
    template_name = 'clubs/club-edit.html'


class ClubDeleteView(ClubsBaseViewMixin, DeleteView):
    form_class = ClubDeleteForm
    template_name = 'clubs/club-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
