from django import forms

from coaches.models import Coach
from common.mixins import DisableFieldsMixin


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'gender', 'birth_date', 'coach_license', 'club', 'photo']

        labels = {
            'name': 'Name:',
            'gender': 'Gender:',
            'birth_date': 'Birth Date:',
            'coach_license': 'Coach License:',
            'club': 'Club:',
            'photo': 'Photo:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter coach name...'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter coach date of birth...'}),
        }


class CoachAddForm(CoachForm):
    ...


class CoachEditForm(CoachForm):
    ...


class CoachDeleteForm(DisableFieldsMixin, CoachForm):
    ...
