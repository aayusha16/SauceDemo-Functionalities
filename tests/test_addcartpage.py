import pytest
import logging
from pages.inventorypage import Inventory
from pages.add_to_cartpage import CartPage

logger = logging.getLogger(__name__)

# Fixture: add products and navigate to cart
@pytest.fixture
def cart_with_products(logged_in_page):
    logger.info("Setting up cart with products")

    inventory = Inventory(logged_in_page)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    for product in products_to_add:
        logger.info(f"Adding product: {product}")
        inventory.add_to_cart(product)

    logger.info("Navigating to cart page")
    inventory.go_to_cart()

    # Wait for cart to load
    logged_in_page.wait_for_selector(".cart_item")

    yield CartPage(logged_in_page)

    logger.info("Teardown: cart fixture completed")


# -------------------- TESTS --------------------

@pytest.mark.cart
def test_cart_products_displayed(cart_with_products):
    """Verify all products added appear in the cart"""
    logger.info("Running test_cart_products_displayed")

    cart = cart_with_products
    products = cart.get_cart_products()

    logger.info(f"Cart contains: {products}")

    assert "Sauce Labs Backpack" in products
    assert "Sauce Labs Bike Light" in products

    logger.info("Test passed: All products displayed correctly")


@pytest.mark.cart
def test_remove_product(cart_with_products):
    """Remove a product and verify cart updates"""
    logger.info("Running test_remove_product")

    cart = cart_with_products

    logger.info("Removing product: Sauce Labs Backpack")
    cart.remove_product("Sauce Labs Backpack")

    products = cart.get_cart_products()
    logger.info(f"Cart after removal: {products}")

    assert "Sauce Labs Backpack" not in products
    assert "Sauce Labs Bike Light" in products

    logger.info("Test passed: Product removed successfully")


@pytest.mark.cart
def test_continue_shopping(cart_with_products):
    """Click Continue Shopping goes back to inventory page"""
    logger.info("Running test_continue_shopping")

    cart = cart_with_products

    logger.info("Clicking Continue Shopping")
    cart.continue_shopping()

    # Better: wait for navigation
    cart.page.wait_for_url("**/inventory.html")

    assert "inventory.html" in cart.page.url

    logger.info("Test passed: Navigated back to inventory page")


@pytest.mark.cart
def test_checkout_navigation(cart_with_products):
    """Click Checkout goes to checkout page"""
    logger.info("Running test_checkout_navigation")

    cart = cart_with_products

    logger.info("Clicking Checkout")
    cart.go_to_checkout()

    # Better: wait for navigation
    cart.page.wait_for_url("**/checkout-step-one.html")

    assert "checkout-step-one.html" in cart.page.url

    logger.info("Test passed: Navigated to checkout page")