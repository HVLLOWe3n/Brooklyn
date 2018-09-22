from django.test import TestCase
from django.urls import reverse

from account.models import User


class LoginTest(TestCase):
    def setUp(self):
        # Create or get usr if he exist
        user = User.objects.create(
            first_name='Roman', last_name='Synovets',
            username='HVLLOWe3n', email='HVLLOWe3n@gmail.com',

        )
        user.save()

    # User go to '/account/login/' and want to login
    def test_when_user_login(self):
        data = {
            'email': 'HVLLOWe3n@gmail.com',
            'username': 'HVLLOWe3n',
            'password': 'MyPass12345',
        }

        self.client.post(reverse('login'), data=data)
        username = self.client.request().POST.get('username')
