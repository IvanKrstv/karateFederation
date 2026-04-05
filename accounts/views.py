from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm, LoginForm
from accounts.tasks import send_welcome_email


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('common:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        send_welcome_email.delay(user.username, user.email)
        return response


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('common:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('common:home')
        return super().dispatch(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('common:home')
