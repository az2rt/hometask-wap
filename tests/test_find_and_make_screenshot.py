
from selenium.webdriver.common.keys import Keys

from pages.main import MainPage

def test_scroll_and_screenshot(browser):
    main_page = MainPage(browser)
    main_page.open()

    main_page.accept_cookies()

    search_btn = main_page.search_btn
    search_btn.click()

    input_fld = main_page.input_fld
    input_fld.send_keys('StarCraft II')
    input_fld.send_keys(Keys.ENTER)

    title = main_page.title_ctg('Videos')
    title.click()

    main_page.scroll_to(2)
    main_page.play_video()

    main_page.make_screenshot()

