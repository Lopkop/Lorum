from django.contrib.auth import get_user_model
from django.test import TestCase

from forum.models import Article


class TestMainForumPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/forum/')

    def test_page_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'forum/home.html')


class TestArticlePage(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Elisabet',
            password='passwordsecret'
        )

        self.article = Article.objects.create(user=self.user, title='100 good news', body='1. I ate some tomato...')
        self.article.save()

        self.response = self.client.get(f'/forum/{self.article.pk}')

    def test_page_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'forum/article.html')

    def test_page_displays_right_article(self):
        self.assertIn(self.article.title.encode(), self.response.content)
        self.assertIn(self.article.body.encode(), self.response.content)
        self.assertIn(str(self.article.user).encode(), self.response.content)
