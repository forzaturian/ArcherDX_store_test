from page_objects.base_page import BasePage
from page_objects.locators import Locators


class CartPage(BasePage):
    def click_plus(self, n):
        self.click_elements(Locators.PLUS, n)

    def click_minus(self, n):
        self.click_elements(Locators.MINUS, n)

    def remove(self, n):
        self.click_elements(Locators.REMOVE, n)

    def proceed_to_checkout(self):
        self.single_click(Locators.CART_CHECKOUT)




