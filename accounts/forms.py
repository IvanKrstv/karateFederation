from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import AppUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    pass
