from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Article, Comment, Like


class TestArticle(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Jessica',
            password='secretpassword123'
        )

    def test_save_and_retrieve(self):
        article = Article.objects.create(user=self.user, title='World, hello!', body='Hello, world!')
        article.save()

        self.assertEqual(str(article), 'World, hello!')
        self.assertEqual(article.body, 'Hello, world!')
        self.assertEqual(article.user, self.user)


class TestComment(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Eric',
            password='passwordsecret321'
        )

        self.article = Article.objects.create(user=self.user, title='Special news!', body='Look here...')
        self.article.save()

    def test_save_and_retrieve(self):
        comment = Comment.objects.create(user=self.user, article=self.article, body='Hello, world!')
        comment.save()

        self.assertEqual(str(comment), 'Hello, world!')
        self.assertEqual(str(comment.user), 'Eric')
        self.assertEqual(comment.article, self.article)


class TestLike(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Lie',
            password='password'
        )

        self.article = Article.objects.create(user=self.user, title='Special news!', body='Look here...')
        self.article.save()

    def test_save_and_retrieve(self):
        like = Like.objects.create(article=self.article, count=5)
        like.save()

        self.assertEqual(str(like), '5')
        self.assertEqual(like.count, 5)
        self.assertEqual(like.article, self.article)