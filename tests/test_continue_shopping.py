from time import sleep


def test_continue_shopping(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    sleep(3)
    app.product.shopping()
    sleep(5)
    assert "Data sheet"