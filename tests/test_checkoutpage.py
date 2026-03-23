import pytest
import logging
from pages.inventorypage import Inventory
from pages.add_to_cartpage import CartPage
from pages.checkout_page import CheckoutPage

logger = logging.getLogger(__name__)

# Fixture: add products and go to checkout page
@pytest.fixture
def checkout_page_with_products(logged_in_page):
    logger.info("Setting up checkout page with products")

    inventory = Inventory(logged_in_page)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    for product in products_to_add:
        logger.info(f"Adding product: {product}")
        inventory.add_to_cart(product)

    logger.info("Navigating to cart page")
    inventory.go_to_cart()

    logged_in_page.wait_for_selector(".cart_item")

    cart = CartPage(logged_in_page)

    logger.info("Clicking checkout button")
    cart.go_to_checkout()

    # Wait for checkout page to load
    logged_in_page.wait_for_selector("#first-name")

    yield CheckoutPage(logged_in_page)

    logger.info("Teardown: checkout fixture completed")


# -------------------- TESTS --------------------

@pytest.mark.checkout
def test_checkout_valid_info(checkout_page_with_products):
    """Enter valid info and continue to overview"""
    logger.info("Running test_checkout_valid_info")

    checkout = checkout_page_with_products

    logger.info("Entering valid checkout details")
    checkout.enter_checkout_info("Aayusha", "Bisunke", "44600")

    logger.info("Clicking continue")
    checkout.continue_checkout()

    # Wait for navigation to overview page
    checkout.page.wait_for_url("**/checkout-step-two.html")

    assert "checkout-step-two.html" in checkout.page.url

    logger.info("Test passed: Successfully navigated to checkout overview")


@pytest.mark.checkout
def test_checkout_cancel(checkout_page_with_products):
    """Cancel checkout and return to cart"""
    logger.info("Running test_checkout_cancel")

    checkout = checkout_page_with_products

    logger.info("Clicking cancel button")
    checkout.cancel_checkout()

    # Wait for navigation back to cart
    checkout.page.wait_for_url("**/cart.html")

    assert "cart.html" in checkout.page.url

    logger.info("Test passed: Successfully returned to cart page")