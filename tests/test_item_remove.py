
def test_remove_an_item(app):
    app.main.add_to_cart(0)
    app.product.add_base_product()
    app.product.checkout()
    app.cart.remove(0)
    assert 'Your shopping cart is empty.'
