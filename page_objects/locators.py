from selenium.webdriver.common.by import By


class Locators:
    ADD_TO_CART = (By.CSS_SELECTOR, '.box-cart-bottom #add_to_cart')
    ELEMENT_1 = (By.CSS_SELECTOR, '.product-container')
    QUANTITY = (By.CSS_SELECTOR, '#quantity_wanted')
    CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    COLOR1 = (By.CSS_SELECTOR, '#color_14')
    COLOR2 = (By.CSS_SELECTOR, '#color_24')
    PRODUCT_ATTRIBUTES = (By.CSS_SELECTOR, '#layer_cart_product_attributes')
    SIZE_M = (By.CSS_SELECTOR, '.selector [value="2"]')
    SIZE_L = (By.CSS_SELECTOR, '.selector [value="3"]')
    SIZE_M2 = (By.CSS_SELECTOR, '#uniform-group_1')
    CHECKOUT = (By.CSS_SELECTOR, 'a.btn.btn-default.button.button-medium')
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, 'span.continue.btn.btn-default.button.exclusive-medium')
    PLUS = (By.CSS_SELECTOR, 'i.icon-plus')
    MINUS = (By.CSS_SELECTOR, 'i.icon-minus')
    REMOVE = (By.CSS_SELECTOR, 'i.icon-trash')
    SHOPPING_CART = (By.CSS_SELECTOR, '.ajax_cart_no_product')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#total_price')
    CART_CHECKOUT = (By.CSS_SELECTOR, '.button.btn.btn-default.standard-checkout.button-medium')


