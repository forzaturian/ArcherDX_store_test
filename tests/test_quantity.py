
def test_null_quantity(app):
    app.main.add_to_cart(0)
    app.product.add_quantity(0)
    app.product.add_base_product()
    assert "Null quantity."


def test_big_quantity(app):
    app.main.add_to_cart(0)
    app.product.add_quantity(1000)
    app.product.add_base_product()
    assert "successfully added to your shopping cart"

