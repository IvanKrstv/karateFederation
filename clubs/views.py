from django.db.models import Prefetch
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from athletes.models import Athlete, Team
from clubs.forms import ClubAddForm, ClubEditForm, ClubDeleteForm, TeamEditForm, TeamDeleteForm, TeamAddForm
from clubs.models import Club


# Create your views here.
class ClubsBaseViewMixin:
    model = Club
    success_url = reverse_lazy('clubs:dashboard')


class ClubsDashboardView(ListView):
    model = Club
    template_name = 'clubs/clubs-dashboard.html'
    context_object_name = 'clubs'
    paginate_by = 6
    
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
            Prefetch(
                'teams',
                queryset=Team.objects.prefetch_related('athletes')
            ),
            'coaches'
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



class TeamAddView(CreateView):
    model = Team
    form_class = TeamAddForm
    template_name = 'teams/team-add.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['club_id'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse(
            'clubs:details',
            kwargs={
                'pk': self.kwargs['pk']
            }
        )


class TeamEditView(UpdateView):
    model = Team
    form_class = TeamEditForm
    template_name = 'teams/team-edit.html'
    pk_url_kwarg = 'team_pk'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['club_id'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse(
            'clubs:details',
            kwargs={
                'pk': self.kwargs['pk']
            }
        )


class TeamDeleteView(DeleteView):
    model = Team
    form_class = TeamDeleteForm
    template_name = 'teams/team-delete.html'
    pk_url_kwarg = 'team_pk'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        kwargs['club_id'] = self.kwargs['pk']
        return kwargs

    def get_success_url(self):
        return reverse(
            'clubs:details',
            kwargs={
                'pk': self.kwargs['pk']
            }
        )