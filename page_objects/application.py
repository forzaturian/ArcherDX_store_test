from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.cart_page import CartPage
# from page_objects.report_page import ReportPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main = MainPage(self)
        self.product = ProductPage(self)
        self.cart = CartPage(self)
