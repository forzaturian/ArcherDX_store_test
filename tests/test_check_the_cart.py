
def test_go_to_shopping_cart(app):
    app.main.shopping_cart()
    assert "Your shopping cart is empty."
