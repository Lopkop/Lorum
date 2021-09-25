from django.test import TestCase


class TestHomePage(TestCase):
    def setUp(self):
        self.response = self.client.get('')

    def test_home_page_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
