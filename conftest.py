import pytest
from selenium import webdriver
from page_objects.application import Application


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('start-fullscreen')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    #driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def app(chrome_browser):
    page = Application(chrome_browser)
    page.main.go_to()
    return page


