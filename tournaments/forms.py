from django import forms

from common.mixins import DisableFieldsMixin
from tournaments.models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'

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
            'teams': forms.SelectMultiple(),
            'name': forms.TextInput(attrs={'placeholder': 'Enter tournament name...'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter tournament country...'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter tournament city...'}),
        }

        error_messages = {
            'name': {
                'max_length': 'The name length must not exceed 50 characters!'
            },
            'country': {
                'max_length': 'There are no country with more than 50 characters!'
            },
            'city': {
                'max_length': 'There are no city with more than 50 characters!'
            }
        }


class TournamentAddForm(TournamentForm):
    ...


class TournamentEditForm(TournamentForm):
    ...


class TournamentDeleteForm(DisableFieldsMixin, TournamentForm):
    ...