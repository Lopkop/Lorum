from django.contrib.auth import get_user_model
from django.test import TestCase

from ..services import create_comment, create_or_delete_like
from ..models import Article, Comment, Like


class TestArticle(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Jessica',
            password='secretpassword123'
        )

        self.article = Article.objects.create(user=self.user, title='World, hello!', body='Hello, world!')
        self.article.save()

    def test_save_and_retrieve(self):
        self.assertEqual(str(self.article), 'World, hello!')
        self.assertEqual(self.article.body, 'Hello, world!')
        self.assertEqual(self.article.user, self.user)

    def test_get_article_comments(self):
        create_comment(self.user, self.article, 'hey!')
        create_comment(self.user, self.article, 'bye!')
        comments = self.article.get_comments(self.article)

        self.assertEqual(2, comments.count())
        self.assertEqual('hey!', comments[0].body)
        self.assertEqual('bye!', comments[1].body)

    def test_get_article_likes(self):
        # Setup second user is necessary, otherwise the function would delete like
        second_user = get_user_model().objects.create_user(
            username='Emma',
            password='secretpassw4'
        )
        create_or_delete_like(self.user, self.article)

        create_or_delete_like(second_user, self.article)

        self.assertEqual(2, self.article.get_likes(self.article).count())


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
        like = Like.objects.create(user=self.user, article=self.article, count=5)
        like.save()

        self.assertEqual(str(like), '5')
        self.assertEqual(like.count, 5)
        self.assertEqual(like.article, self.article)
