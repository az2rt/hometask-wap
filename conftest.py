import pytest
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser():
    chromedriver_autoinstaller.install()

    mobile_emulation = {
            "deviceMetrics": {"width": 412, "height": 915, "pixelRation": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                         " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
            "clientHints": {"platform": "Android", "mobile": True}
    }
    options = Options()
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    options.add_experimental_option(
        "prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": False,
            "javascript.enabled": True,
            "profile.content_settings.exceptions.clipboard": {"*": {"setting": 1}},
        }
    )

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()
