from django.contrib.auth import get_user_model
from django.test import TestCase

from forum.models import Article
from ..services import create_comment, create_article, get_article_comments


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

        create_article(user=self.user, title='100 good news', body='1. I ate some tomato...')
        self.article = Article.objects.all()[0]
        self.response = self.client.get(f'/forum/{self.article.pk}')

    def test_page_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'forum/article.html')

    def test_page_displays_right_article(self):
        self.assertIn(self.article.title.encode(), self.response.content)
        self.assertIn(self.article.body.encode(), self.response.content)
        self.assertIn(str(self.article.user).encode(), self.response.content)

    def test_comments_displays_on_the_page(self):
        text = 'hahaha'
        second_text = 'no no no'

        create_comment(self.user, self.article, text)
        create_comment(self.user, self.article, second_text)

        comment, second_comment = get_article_comments(self.article)

        # Refresh the page to see comments
        response = self.client.get(f'/forum/{self.article.pk}')

        self.assertEqual(text, comment.body)
        self.assertEqual(second_text, second_comment.body)
        self.assertIn(comment.body.encode(), response.content)
        self.assertIn(second_comment.body.encode(), response.content)
