from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage(object):

    def __init__(self, app, wait=5):
        self.app = app
        self.base_url = "http://automationpractice.com/index.php"
        self.wait = WebDriverWait(self.app.driver, wait)
        self.actions = ActionChains(app.driver)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def single_click(self, locator):
        self.find_element(locator).click()

    def click_elements(self, locator, n):
        r = self.find_elements(locator)
        r[n].click()

    def find_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    def reach_element(self, locator):
        a = self.find_elements(locator)
        return self.actions.move_to_element(a)

    def clear(self, locator):
        self.find_element(locator).clear()

    def input(self, locator, key):
        self.find_element(locator).send_keys(key)

    def go_to(self):
        return self.app.driver.get(self.base_url)

    def alert(self):
        return self.app.driver.switch_to_alert().accept()
