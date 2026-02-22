from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search clubs...' # In the future a feature for searching also athletes and coaches can be added
        })
    )