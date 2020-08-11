from page_objects.base_page import BasePage
from page_objects.locators import Locators


class ProductPage(BasePage):
    def add_base_product(self):
        self.single_click(Locators.ADD_TO_CART)

    def add_quantity(self, q):
        self.clear(Locators.QUANTITY)
        self.input(Locators.QUANTITY, q)

    def new_color(self):
        self.single_click(Locators.COLOR1)

    def new_color2(self):
        self.single_click(Locators.COLOR2)

    def get_text(self, text):
        self.find_text(Locators.PRODUCT_ATTRIBUTES, text)

    def size_change(self):
        self.single_click(Locators.SIZE_M)

    def size2_change(self):
        self.single_click(Locators.SIZE_M2)

    def checkout(self):
        self.single_click(Locators.CHECKOUT)

    def shopping(self):
        self.single_click(Locators.CONTINUE_SHOPPING)










