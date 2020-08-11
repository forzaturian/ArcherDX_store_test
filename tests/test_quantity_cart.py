
def test_cart_quantity_inc(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    app.product.checkout()
    app.cart.click_plus(0)
    assert '2'


def test_cart_quantity_dec(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    app.product.checkout()
    app.cart.click_minus(0)
    assert 'Your shopping cart is empty.'
