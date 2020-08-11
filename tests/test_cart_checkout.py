from time import sleep


def test_proceed_to_checkout(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.checkout()
    app.cart.proceed_to_checkout()
    sleep(3)
    assert "Create an account"