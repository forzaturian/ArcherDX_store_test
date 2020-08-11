
def test_continue_shopping(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    app.product.shopping()
    assert "Data sheet"
