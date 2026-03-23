import pytest
import logging
from pages.inventorypage import Inventory

logger = logging.getLogger(__name__)


# -------------------- TESTS --------------------

@pytest.mark.inventory
def test_products_are_displayed(logged_in_page):
    """Verify that products are visible on the inventory page"""
    logger.info("Running test_products_are_displayed")

    inventory = Inventory(logged_in_page)

    products = inventory.get_product_list()
    logger.info(f"Products on page: {products}")

    assert len(products) > 0

    logger.info("Test passed: Products are displayed")


@pytest.mark.inventory
def test_add_single_product(logged_in_page):
    """Add a single product to the cart and verify cart count"""
    logger.info("Running test_add_single_product")

    inventory = Inventory(logged_in_page)

    logger.info("Adding product: Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Backpack")

    cart_count = inventory.get_cart_count()
    logger.info(f"Cart count: {cart_count}")

    assert cart_count == 1

    logger.info("Test passed: Single product added successfully")


@pytest.mark.inventory
def test_add_multiple_products(logged_in_page):
    """Add multiple products dynamically and verify cart count"""
    logger.info("Running test_add_multiple_products")

    inventory = Inventory(logged_in_page)

    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]

    for product in products_to_add:
        logger.info(f"Adding product: {product}")
        inventory.add_to_cart(product)

    cart_count = inventory.get_cart_count()
    logger.info(f"Cart count: {cart_count}")

    assert cart_count == len(products_to_add)

    logger.info("Test passed: Multiple products added successfully")


@pytest.mark.inventory
def test_remove_product(logged_in_page):
    """Add a product and then remove it, verifying the cart updates"""
    logger.info("Running test_remove_product")

    inventory = Inventory(logged_in_page)

    logger.info("Adding product: Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Backpack")

    assert inventory.get_cart_count() == 1

    logger.info("Removing product: Sauce Labs Backpack")
    inventory.remove_from_cart("Sauce Labs Backpack")

    cart_count = inventory.get_cart_count()
    logger.info(f"Cart count after removal: {cart_count}")

    assert cart_count == 0

    logger.info("Test passed: Product removed successfully")


@pytest.mark.inventory
def test_cart_navigation(logged_in_page):
    """Verify clicking the cart icon navigates to the cart page"""
    logger.info("Running test_cart_navigation")

    inventory = Inventory(logged_in_page)

    logger.info("Clicking cart icon")
    inventory.go_to_cart()

    # Wait for navigation (important)
    logged_in_page.wait_for_url("**/cart.html")

    assert "cart.html" in logged_in_page.url

    logger.info("Test passed: Navigation to cart page successful")