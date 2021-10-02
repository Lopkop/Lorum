from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from config.settings import values


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        # options.add_argument('--headless')
        self.browser = webdriver.Firefox(executable_path=values.get('GECKODRIVER_PATH'), options=options)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
