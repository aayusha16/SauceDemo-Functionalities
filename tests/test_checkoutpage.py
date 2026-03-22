import pytest
from pages.inventorypage import Inventory
from pages.add_to_cartpage import CartPage
from pages.checkout_page import CheckoutPage

# Fixture: add products and go to checkout page
@pytest.fixture
def checkout_page_with_products(logged_in_page):
    inventory = Inventory(logged_in_page)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    for product in products_to_add:
        inventory.add_to_cart(product)

    inventory.go_to_cart()

    logged_in_page.wait_for_selector(".cart_item")

    cart = CartPage(logged_in_page)
    cart.go_to_checkout()

    logged_in_page.wait_for_selector("#first-name")  # wait until checkout page loads
    yield CheckoutPage(logged_in_page)


@pytest.mark.checkout
def test_checkout_valid_info(checkout_page_with_products):
    """Enter valid info and continue to overview"""
    checkout = checkout_page_with_products
    checkout.enter_checkout_info("Aayusha", "Bisunke", "44600")
    checkout.continue_checkout()
    assert "checkout-step-two.html" in checkout.page.url


@pytest.mark.checkout
def test_checkout_cancel(checkout_page_with_products):
    """Cancel checkout and return to cart"""
    checkout = checkout_page_with_products
    checkout.cancel_checkout()
    assert "cart.html" in checkout.page.url