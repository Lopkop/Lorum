from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_user_can_send_messages_on_the_forum(self):
        # John has heard about a cool new online forum.
        # He goes to check out its homepage.
        self.browser.get(self.live_server_url)

        # He notices that the homepage is explaining the meaning of the project "Lorum".
        self.assertEqual(self.browser.title, 'Lorum Project')
        self.assertIn('Lorum', self.browser.find_element_by_tag_name('h1').text)

        # He is invited to enter a forum straight away...
        self.browser.find_element_by_id('id-forum').click()
        self.assertEqual(self.browser.title, 'Forum')
