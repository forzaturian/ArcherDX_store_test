from time import sleep


def test_proceed_to_checkout(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.checkout()
    sleep(5)
    assert "Shopping-cart summary"

