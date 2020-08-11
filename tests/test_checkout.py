
def test_proceed_to_checkout(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    app.product.checkout()
    assert "Shopping-cart summary"

