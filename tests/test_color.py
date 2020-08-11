
def test_change_color(app):
    app.main.add_to_cart(0)
    app.product.new_color()
    app.product.add_base_product()
    assert 'Blue, S'


def test_change_color_and_size(app):
    app.main.add_to_cart(3)
    app.product.new_color2()
    app.product.size2_change()
    app.product.add_base_product()
    assert 'Pink, M'
