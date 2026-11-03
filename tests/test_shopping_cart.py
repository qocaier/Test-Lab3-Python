import pytest
from src.shopping_cart import Product
from src.shopping_cart import ShoppingCart


def test_add_item_success():
    product = Product("prod_1", "Смартфон", 50000.0, 10)
    cart = ShoppingCart()
    cart.add_item(product, 2)
    assert cart.items["prod_1"]["quantity"] == 2


def test_add_item_invalid_quantity():
    product = Product("prod_1", "Смартфон", 50000.0, 10)
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(product, 0)
    with pytest.raises(ValueError):
        cart.add_item(product, -1)


def test_add_item_exceed_stock():
    product = Product("prod_1", "Смартфон", 50000.0, 5)
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item(product, 6)


def test_remove_item():
    product = Product("prod_1", "Смартфон", 50000.0, 10)
    cart = ShoppingCart()
    cart.add_item(product, 5)
    cart.remove_item("prod_1", 2)
    assert cart.items["prod_1"]["quantity"] == 3
    cart.remove_item("prod_1")
    assert "prod_1" not in cart.items


def test_total_price_and_promo():
    product1 = Product("prod_1", "Товар 1", 100.0, 10)
    product2 = Product("prod_2", "Товар 2", 200.0, 10)
    cart = ShoppingCart()
    cart.add_item(product1, 2)
    cart.add_item(product2, 1)
    assert cart.get_total_price() == 400.0
    cart.apply_promo("DISCOUNT10")
    assert cart.get_total_price() == 360.0
    with pytest.raises(ValueError):
        cart.apply_promo("WRONGCODE")