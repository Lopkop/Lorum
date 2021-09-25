from django.test import TestCase


class TestMainForumPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/forum/')

    def test_page_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'forum/home.html')
