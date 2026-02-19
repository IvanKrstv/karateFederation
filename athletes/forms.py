from django import forms

from athletes.models import Athlete
from common.mixins import DisableFieldsMixin


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'gender', 'birth_date', 'belt', 'club', 'photo']

        labels = {
            'name': 'Name:',
            'gender': 'Gender:',
            'birth_date': 'Birth Date:',
            'belt': 'Belt:',
            'club': 'Club:',
            'photo': 'Photo:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter athlete name...'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter athlete date of birth...'}),
        }


class AthleteAddForm(AthleteForm):
    pass


class AthleteEditForm(AthleteForm):
    pass


class AthleteDeleteForm(DisableFieldsMixin, AthleteForm):
    pass
