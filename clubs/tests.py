from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.test import TestCase
from django.urls import reverse

from clubs.models import Club

UserModel = get_user_model()


def create_club():
    return Club.objects.create(
        name='Shotokan',
        founder_name='John Doe',
        country='Bulgaria',
        city='Sofia',
    )


class ClubsDashboardViewTests(TestCase):
    def test_dashboard_accessible_to_anonymous_user(self):
        response = self.client.get(reverse('clubs:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_shows_clubs(self):
        create_club()
        response = self.client.get(reverse('clubs:dashboard'))
        self.assertContains(response, 'Shotokan')


class ClubAddViewTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='StrongPass123!')

    def test_add_club_redirects_anonymous_to_login(self):
        response = self.client.get(reverse('clubs:add'))
        self.assertRedirects(response, f"{reverse('accounts:login')}?next={reverse('clubs:add')}")

    def test_add_club_forbidden_for_user_without_permission(self):
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(reverse('clubs:add'))
        self.assertEqual(response.status_code, 403)

    def test_add_club_accessible_with_permission(self):
        permission = Permission.objects.get(codename='add_club')
        self.user.user_permissions.add(permission)
        self.client.login(username='testuser', password='StrongPass123!')
        response = self.client.get(reverse('clubs:add'))
        self.assertEqual(response.status_code, 200)


class ClubDeleteViewTests(TestCase):
    def setUp(self):
        self.club = create_club()
        self.editor = UserModel.objects.create_user(username='editor', password='StrongPass123!')
        editor_group = Group.objects.create(name='TestEditor')
        for codename in ['add_club', 'change_club', 'view_club']:
            editor_group.permissions.add(Permission.objects.get(codename=codename))
        self.editor.groups.add(editor_group)

    def test_delete_club_forbidden_for_editor(self):
        self.client.login(username='editor', password='StrongPass123!')
        response = self.client.get(reverse('clubs:delete', kwargs={'pk': self.club.pk}))
        self.assertEqual(response.status_code, 403)
