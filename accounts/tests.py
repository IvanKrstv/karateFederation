from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class RegisterViewTests(TestCase):
    def test_register_creates_user(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(UserModel.objects.count(), 1)
        self.assertEqual(UserModel.objects.first().username, 'testuser')

    def test_register_duplicate_username_fails(self):
        UserModel.objects.create_user(username='testuser', password='StrongPass123!')
        response = self.client.post(reverse('accounts:register'), {
            'username': 'testuser',
            'email': 'other@test.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserModel.objects.count(), 1)

    def test_authenticated_user_redirected_from_register(self):
        UserModel.objects.create_user(username='testuser', password='StrongPass123!')
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(reverse('accounts:register'))
        self.assertRedirects(response, reverse('common:home'))


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='StrongPass123!')

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'StrongPass123!',
        })
        self.assertRedirects(response, reverse('common:home'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_authenticated_user_redirected_from_login(self):
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(reverse('accounts:login'))
        self.assertRedirects(response, reverse('common:home'))


class LogoutViewTests(TestCase):
    def test_logout_redirects_to_login(self):
        user = UserModel.objects.create_user(username='testuser', password='StrongPass123!')
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('common:home'))
