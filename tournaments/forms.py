from django import forms

from common.mixins import DisableFieldsMixin
from tournaments.models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
        exclude = ['created_at',]

        labels = {
            'name': 'Name:',
            'date': 'Date:',
            'country': 'Country:',
            'city': 'City:',
            'photo': 'Photo:'
        }

        help_texts = {
            'teams': 'Choose the teams which take part in the competition...'
        }

        widgets = {
            'teams': forms.SelectMultiple()
        }


class TournamentAddForm(TournamentForm):
    ...


class TournamentEditForm(TournamentForm):
    ...


class TournamentDeleteForm(DisableFieldsMixin, TournamentForm):
    ...