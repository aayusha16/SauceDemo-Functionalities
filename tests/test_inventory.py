import pytest
from pages.inventorypage import Inventory

@pytest.mark.inventory
def test_products_are_displayed(logged_in_page):
    """Verify that products are visible on the inventory page"""
    inventory = Inventory(logged_in_page)
    products = inventory.get_product_list()
    assert len(products) > 0
    print("Products on page:", products)


@pytest.mark.inventory
def test_add_single_product(logged_in_page):
    """Add a single product to the cart and verify cart count"""
    inventory = Inventory(logged_in_page)
    inventory.add_to_cart("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1


@pytest.mark.inventory
def test_add_multiple_products(logged_in_page):
    """Add multiple products dynamically and verify cart count"""
    inventory = Inventory(logged_in_page)
    products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    for product in products_to_add:
        inventory.add_to_cart(product)
    assert inventory.get_cart_count() == len(products_to_add)


@pytest.mark.inventory
def test_remove_product(logged_in_page):
    """Add a product and then remove it, verifying the cart updates"""
    inventory = Inventory(logged_in_page)
    inventory.add_to_cart("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1

    inventory.remove_from_cart("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 0


@pytest.mark.inventory
def test_cart_navigation(logged_in_page):
    """Verify clicking the cart icon navigates to the cart page"""
    inventory = Inventory(logged_in_page)
    inventory.go_to_cart()
    assert "cart.html" in logged_in_page.url