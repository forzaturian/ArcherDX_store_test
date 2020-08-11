from time import sleep


def test_go_to_shopping_cart(app):
    app.main.shopping_cart()
    sleep(5)
    assert "Your shopping cart is empty."
