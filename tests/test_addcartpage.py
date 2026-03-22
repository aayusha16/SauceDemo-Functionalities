import pytest
from pages.inventorypage import Inventory
from pages.add_to_cartpage import CartPage

# Fixture: add products and navigate to cart
@pytest.fixture
def cart_with_products(logged_in_page):
    inventory = Inventory(logged_in_page)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    for product in products_to_add:
        inventory.add_to_cart(product)

    inventory.go_to_cart()
    logged_in_page.wait_for_selector(".cart_item")  # ensure cart loaded

    yield CartPage(logged_in_page)


@pytest.mark.cart
def test_cart_products_displayed(cart_with_products):
    """Verify all products added appear in the cart"""
    cart = cart_with_products
    products = cart.get_cart_products()
    assert "Sauce Labs Backpack" in products
    assert "Sauce Labs Bike Light" in products


@pytest.mark.cart
def test_remove_product(cart_with_products):
    """Remove a product and verify cart updates"""
    cart = cart_with_products
    cart.remove_product("Sauce Labs Backpack")
    products = cart.get_cart_products()
    assert "Sauce Labs Backpack" not in products
    assert "Sauce Labs Bike Light" in products


@pytest.mark.cart
def test_continue_shopping(cart_with_products):
    """Click Continue Shopping goes back to inventory page"""
    cart = cart_with_products
    cart.continue_shopping()
    assert "inventory.html" in cart.page.url  # fixed assertion


@pytest.mark.cart
def test_checkout_navigation(cart_with_products):
    """Click Checkout goes to checkout page"""
    cart = cart_with_products
    cart.go_to_checkout()
    assert "checkout-step-one.html" in cart.page.url