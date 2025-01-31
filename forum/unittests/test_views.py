from django.contrib.auth import get_user_model
from django.test import TestCase

from forum.models import Article
from ..services import create_comment, create_article, create_or_delete_like


class TestMainForumPage(TestCase):
    def setUp(self):
        self.response = self.client.get('/forums/')

    def test_page_works(self):
        self.assertEqual(200, self.response.status_code)

    def test_uses_right_template(self):
        self.assertTemplateUsed(self.response, 'forum/home.html')


class TestArticlePage(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Elisabet',
            password='passwordsecret'
        )

        create_article(user=self.user, title='100 good news', body='1. I ate some tomato...', category='other')
        self.article = Article.objects.all()[0]
        self.response = self.client.get(f'/forums/other/{self.article.pk}')

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

        comment, second_comment = self.article.get_comments(self.article)

        # Refresh the page to see comments
        response = self.client.get(f'/forums/other/{self.article.pk}')

        self.assertEqual(text, comment.body)
        self.assertEqual(second_text, second_comment.body)
        self.assertIn(comment.body.encode(), response.content)
        self.assertIn(second_comment.body.encode(), response.content)

    def test_likes_displays_on_the_page(self):
        second_user = get_user_model().objects.create_user(
            username='Emma',
            password='secretpassw4'
        )

        create_or_delete_like(self.user, self.article)
        create_or_delete_like(second_user, self.article)

        # Refresh the page to see likes
        response = self.client.get(f'/forums/other/{self.article.pk}')

        self.assertIn('2'.encode(), response.content)


class TestAllCategories(TestCase):
    def category_test(self, name):
        response = self.client.get(f'/forums/{name}/')

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, f'forum/{name}.html')
        self.assertContains(response, name.capitalize())

    def test_programming_category(self):
        self.category_test('programming')

    def test_security_category(self):
        self.category_test('security')

    def test_math_category(self):
        self.category_test('mathematics')

    def test_physics_category(self):
        self.category_test('physics')

    def test_electronics_category(self):
        self.category_test('electronics')

    def test_other_category(self):
        self.category_test('other')
