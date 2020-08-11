from page_objects.base_page import BasePage
from page_objects.locators import Locators


class MainPage(BasePage):
    def add_to_cart(self, n):
        self.click_elements(Locators.ELEMENT_1, n)

    def shopping_cart(self):
        self.single_click(Locators.SHOPPING_CART)
