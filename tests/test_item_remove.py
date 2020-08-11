from time import sleep


def test_remove_an_item(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.checkout()
    sleep(3)
    app.cart.remove(0)
    sleep(3)
    assert 'Your shopping cart is empty.'
    sleep(2)
