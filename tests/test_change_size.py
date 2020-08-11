
def test_add_product(app):
    app.main.add_to_cart(0)
    app.product.size_change()
    app.product.add_base_product()
    assert 'Orange, M'

