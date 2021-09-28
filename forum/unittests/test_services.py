from django.contrib.auth import get_user_model
from django.test import TestCase

from forum.models import Article, Comment, Like
from ..services import (create_comment,
                        create_article,
                        get_article_comments,
                        get_article,
                        create_or_delete_like,
                        get_article_likes
                        )


class TestServices(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Elisabet',
            password='passwordsecret'
        )

        self.article = Article.objects.create(user=self.user, title='World, hello!', body='Hello, world!')
        self.article.save()
        self.response = self.client.get(f'/forum/{self.article.pk}')

    def test_create_comment(self):
        create_comment(self.user, self.article, 'lol')

        self.assertEqual(1, Comment.objects.all().count())
        self.assertEqual('lol', Comment.objects.all()[0].body)

    def test_create_article(self):
        create_article(self.user, 'NO', 'YES')

        # 2 articles because 1 we create in the setUp and 1 here
        self.assertEqual(2, Article.objects.all().count())
        self.assertEqual('NO', Article.objects.all()[1].title)
        self.assertEqual('YES', Article.objects.all()[1].body)

    def test_create_like(self):
        create_or_delete_like(self.user, self.article)

        self.assertEqual(1, Like.objects.all().count())

    def test_delete_like(self):
        create_or_delete_like(self.user, self.article)
        create_or_delete_like(self.user, self.article)

        self.assertEqual(0, Like.objects.all().count())

    def test_get_article_comments(self):
        create_comment(self.user, self.article, 'hey!')
        create_comment(self.user, self.article, 'bye!')
        comments = get_article_comments(self.article)

        self.assertEqual(2, comments.count())
        self.assertEqual('hey!', comments[0].body)
        self.assertEqual('bye!', comments[1].body)

    def test_get_article(self):
        self.assertEqual(self.article, get_article(self.article.pk))

    def test_get_article_likes(self):
        # Setup second user is necessary, otherwise the function would delete like
        second_user = get_user_model().objects.create_user(
            username='Emma',
            password='secretpassw4'
        )
        create_or_delete_like(self.user, self.article)

        create_or_delete_like(second_user, self.article)

        self.assertEqual(2, get_article_likes(self.article).count())
