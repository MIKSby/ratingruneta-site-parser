from selenium.webdriver.firefox.webdriver import WebDriver, FirefoxProfile
import os


class FirefoxDriver(WebDriver):
    def __init__(self):
        os.environ['PATH'] += os.pathsep + os.getcwd() + '/'
        super().__init__()

    def run_browser(self):
        return WebDriver(firefox_profile=self._set_profile())

    @staticmethod
    def _set_profile():
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        profile = FirefoxProfile()
        profile.set_preference('general.useragent.override', useragent)
        return profile
