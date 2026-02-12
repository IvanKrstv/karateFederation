from django import forms

from clubs.models import Club
from common.mixins import DisableFieldsMixin


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        exclude = ['slug', 'created_at']

        labels = {
            'name': 'Club name:',
            'founder_name': 'Club founder:',
            'country': 'Country:',
            'city': 'City:',
            'photo': 'Logo:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter club name...'}),
            'founder_name': forms.TextInput(attrs={'placeholder': 'Enter club founder...'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter club country...'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter club city...'}),
        }

        error_messages = {
            'name': {

            },
            'founder_name': {

            },
            'country': {

            },
            'city': {

            }
        }


class ClubAddForm(ClubForm):
    ...


class ClubEditForm(ClubForm):
    ...


class ClubDeleteForm(DisableFieldsMixin, ClubForm):
    ...


