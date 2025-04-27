import pytest
from selenium.webdriver import Firefox

import curl
from curl import *

@pytest.fixture
def driver():
    browser = Firefox()
    browser.get(main_page)
    yield browser
    browser.quit()

@pytest.fixture
def to_order_page(driver):
    driver.get(curl.order_page)
    return driver

