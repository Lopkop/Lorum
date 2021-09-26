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

        self.article = Article.objects.create(user=self.user, title='100 good news', body='1. I ate some tomato...')
        self.article.save()

        super().setUp()

    def test_user_can_send_messages_on_the_forum(self):
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
        self.browser.find_element_by_id('article-id').click()
        sleep(5)
        self.assertEqual('100 good news', self.browser.title)

        # He wants to chat with other people about this article...
