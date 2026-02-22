from django import forms

from clubs.models import Club
from common.mixins import DisableFieldsMixin


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        exclude = ['created_at']

        labels = {
            'name': 'Club name:',
            'founder_name': 'Club founder:',
            'country': 'Country:',
            'city': 'City:',
            'photo': 'Logo:',
            'slug': 'Slug:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter club name...'}),
            'founder_name': forms.TextInput(attrs={'placeholder': 'Enter club founder name...'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter club country...'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter club city...'}),
        }

        error_messages = {
            'name': {
                'max_length': 'The name length must not exceed 50 characters!'
            },
            'founder_name': {
                'max_length': 'The name length must not exceed 50 characters!'
            },
            'country': {
                'max_length': 'There are no country with more than 50 characters!'
            },
            'city': {
                'max_length': 'There are no city with more than 50 characters!'
            }
        }


class ClubAddForm(ClubForm):
    ...


class ClubEditForm(ClubForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].disabled = True


class ClubDeleteForm(DisableFieldsMixin, ClubForm):
    ...


