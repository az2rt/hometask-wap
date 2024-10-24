from .base import BasePage
import polling2
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def search_btn(self):
        return self.find_element(".//a[@aria-label='Search']")

    @property
    def input_fld(self):
        return self.find_element(".//input[@placeholder='Search...']")

    @property
    def video(self):
        return self.find_element("(.//a[contains(@class, 'ScCoreLink')])[6]")

    @property
    def spinner(self):
        return self.find_element(".//span[contains(@class, 'ScSpinner')]")

    @property
    def subscribe_btn(self):
        return self.find_element(".//*[contains(@data-a-target, 'core-button') and text()='Subscribe']")

    def title_ctg(self, name):
        return self.find_element(f".//div[contains(@class, 'ScTitle') and text()='{name}']")

    def accept_cookies(self):
        cookie_banner = self.find_element(".//*[contains(@class, 'Layout') and text()='Accept']")
        if cookie_banner.is_displayed():
                self.browser.execute_script("""
                       let cookiePopup = document.evaluate(
                           './/div[contains(@class, "consent-banner__content")]',
                           document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
                       ).singleNodeValue;

                       if (cookiePopup) {
                           cookiePopup.parentElement.remove();
                       }
                   """)

    def play_video(self):
        # this method is needed to avoid videos from streamers
        # that are only available after subscription
        self.video.click()
        try:
            if self.subscribe_btn.is_displayed():
                self.browser.back()
                self.scroll_to(2)
                self.video.click()
        except TimeoutException:
            pass
        finally:
            self.check_video()

    def check_video(self, wait=5):
        from selenium.webdriver.common.by import By
        video = self.find_element('.//video')
        polling2.poll(
            lambda: self.browser.execute_script('return arguments[0].currentTime;', video) > 2,
            timeout=wait,
            step=3,
        )
