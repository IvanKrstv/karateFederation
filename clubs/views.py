from django.db.models import Prefetch
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from athletes.models import Athlete
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
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('query')

        if query:
            qs = qs.filter(name__icontains=query)

        return qs


class ClubDetailView(DetailView):
    model = Club
    template_name = 'clubs/club-details.html'

    def get_queryset(self):
        qs = Club.objects.prefetch_related(
            Prefetch(
                'athletes',
                queryset=Athlete.objects.prefetch_related('teams')
            ),
            'coaches',
            'athletes'
        )

        return qs



class ClubAddView(ClubsBaseViewMixin, CreateView):
    form_class = ClubAddForm
    template_name = 'clubs/club-add.html'


class ClubEditView(UpdateView):
    model = Club
    form_class = ClubEditForm
    template_name = 'clubs/club-edit.html'

    def get_success_url(self):
        return reverse(
            'clubs:details',
            kwargs={
                'pk':self.object.pk
            }
        )


class ClubDeleteView(ClubsBaseViewMixin, DeleteView):
    form_class = ClubDeleteForm
    template_name = 'clubs/club-delete.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs
