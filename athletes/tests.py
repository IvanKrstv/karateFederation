from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from athletes.models import Athlete
from clubs.models import Club

UserModel = get_user_model()


def create_club():
    return Club.objects.create(
        name='Shotokan',
        founder_name='John Doe',
        country='Bulgaria',
        city='Sofia',
    )


def create_athlete(club, name='Ivan Ivanov', belt='Black', gender='M'):
    return Athlete.objects.create(
        name=name,
        gender=gender,
        birth_date='2000-01-01',
        belt=belt,
        club=club,
    )


class AthletesAPITests(TestCase):
    def setUp(self):
        self.club = create_club()
        create_athlete(self.club, name='Ivan Ivanov', belt='Black', gender='M')
        create_athlete(self.club, name='Maria Petrova', belt='White', gender='F')

    def test_athletes_list_returns_200(self):
        response = self.client.get(reverse('athletes:api-list'))
        self.assertEqual(response.status_code, 200)

    def test_athletes_list_returns_all(self):
        response = self.client.get(reverse('athletes:api-list'))
        self.assertEqual(len(response.data), Athlete.objects.count())

    def test_filter_by_belt(self):
        response = self.client.get(reverse('athletes:api-list'), {'belt': 'black', 'club_id': self.club.pk})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Ivan Ivanov')

    def test_filter_by_gender(self):
        response = self.client.get(reverse('athletes:api-list'), {'gender': 'f', 'club_id': self.club.pk})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Maria Petrova')

    def test_filter_by_club_id(self):
        response = self.client.get(reverse('athletes:api-list'), {'club_id': self.club.pk})
        self.assertEqual(len(response.data), 2)

    def test_unauthenticated_user_cannot_post(self):
        response = self.client.post(reverse('athletes:api-list'), {
            'name': 'New Athlete',
            'gender': 'M',
            'birth_date': '2000-01-01',
            'belt': 'White',
            'club_id': self.club.pk,
        })
        self.assertEqual(response.status_code, 403)
