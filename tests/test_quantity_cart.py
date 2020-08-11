from time import sleep


def test_cart_quantity_inc(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.checkout()
    sleep(3)
    app.cart.click_plus(0)
    sleep(3)
    assert '2'


def test_cart_quantity_dec(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.checkout()
    sleep(3)
    app.cart.click_minus(0)
    sleep(3)
    assert 'Your shopping cart is empty.'
    sleep(2)
