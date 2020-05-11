from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from .models import Profile


class ViewsTests(TestCase):
    def setUp(self):
        data = {
            'username': 'test_user',
            'password1': 'Password_01234',
            'password2': 'Password_01234'
        }
        self.client = Client()
        resp = self.client.post(
            reverse('accounts:sign_up'),
            data=data
        )
        self.assertEqual(resp.status_code, 302)

    def test_singin(self):
        user_data = {
            'username': 'test_user',
            'password': 'Password_01234'
        }
        resp = self.client.post(
            reverse('accounts:sign_in'),
            data=user_data
        )
        self.assertEqual(resp.status_code, 302)

    def test_bad_singin(self):
        user_data = {
            'username': 'test_user',
            'password': 'invalid_password'
        }
        resp = self.client.post(
            reverse('accounts:sign_in'),
            data=user_data
        )
        self.assertEqual(resp.status_code, 200)

    def test_singout(self):
        resp = self.client.get(reverse('accounts:sign_out'))
        self.assertEqual(resp.status_code, 302)

    def test_edit_profile(self):
        user_data = {
            'username': 'test_user',
            'password': 'Password_01234'
        }
        resp = self.client.post(
            'accounts/sign_in',
            data=user_data
        )
        profile_data = {
            'first_name': 'Luke',
            'last_name': 'Skywalker',
            'date_of_birth': '1977-05-25',
            'bio': 'I am a Jedi.',
            'country': 'Tatooine',
            'favorite_animal': 'R2-D2',
            'hobby': 'Aircraft',
            'email': 'skywalker@force.com',
            'confirmed_email': 'skywalker@force.com'
        }
        resp = self.client.post(
            reverse('accounts:edit_profile'),
            data=user_data
        )
        self.assertEqual(resp.status_code, 200)

    def test_view_profile(self):
        resp = self.client.get(reverse('accounts:profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounts/profile.html')

    def test_change_password(self):
        password_data = {
            'old_passswprd': 'Password_01234',
            'new_password1': 'New_Password_9999',
            'new_password2': 'New_Password_9999'
        }
        resp = self.client.post(
            reverse('accounts:change_password'),
            data=password_data
        )
        self.assertEqual(resp.status_code, 200)
