from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://m.twitch.tv"

    def open(self, path=""):
        self.browser.get(self.base_url + path)

    def find_element(self, value="", by=By.XPATH, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def execute_script(self, script, value=None):
        return self.browser.execute_script(script, value) if value else self.browser.execute_script(script)

    def scroll_to(self, repeat: int=1):
        for _ in range(repeat):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def make_screenshot(self):
        return self.browser.get_screenshot_as_file('test.png')

