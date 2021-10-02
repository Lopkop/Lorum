from time import sleep

from django.contrib.auth import get_user_model

from forum.models import Article
from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Elisabet',
            password='passwordsecret'
        )

        self.article = Article.objects.create(user=self.user, title='100 good news', body='1. I ate some tomato...', category='programming')
        self.article.save()

        super().setUp()

    def test_user_cannot_send_message_or_like_on_the_forum_while_logged_out(self):
        # John has heard about a cool new online forum.
        # He goes to check out its homepage.
        self.browser.get(self.live_server_url)

        # He notices that the homepage is explaining the meaning of the project "Lorum".
        self.assertEqual('Lorum Project', self.browser.title)
        self.assertIn('Lorum', self.browser.find_element_by_tag_name('h1').text)

        # He is invited to enter a forum straight away...
        self.browser.find_element_by_id('id-forum').click()
        self.assertEqual('Forum', self.browser.title)

        # He found an interesting article and wants to read about this topic...
        self.browser.find_element_by_id('articles_1').click()

        self.browser.find_element_by_id('article-id').click()
        sleep(1)
        self.assertEqual('100 good news', self.browser.title)

        # He wants to write comment about this article...
        input_box = self.browser.find_element_by_id('id_body')
        input_box.send_keys('very interesting article!')
        self.browser.find_element_by_id('comment-id').click()
        sleep(1)

        # but unfortunately, he is not logged in on the website
        self.assertEqual(
            "Sorry, but you can't comment or like any post in security concerns, because you are not logged in.",
            self.browser.find_element_by_id('id-error').text)

        # He step back...
        self.browser.back()

        # and just want to like this article...
        self.browser.find_element_by_id('like-id').click()
        sleep(1)

        # but unfortunately, the same error is raised.
        self.assertEqual(
            "Sorry, but you can't comment or like any post in security concerns, because you are not logged in.",
            self.browser.find_element_by_id('id-error').text)
