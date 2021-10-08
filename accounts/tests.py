from django.contrib.auth import get_user_model
from django.test import TestCase


class TestAccounts(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Elisabet',
            password='passwordsecret'
        )

        self.response = self.client.get(f'/accounts/{self.user.pk}')

    def test_user_page_display_username(self):
        self.assertIn(b'Elisabet', self.response.content)
