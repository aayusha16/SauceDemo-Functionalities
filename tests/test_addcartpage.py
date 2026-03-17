from pages.loginpage import Login
from pages.inventorypage import InventoryPage
from pages.cart_page import CartPage

def test_cart_items_match_added(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    # Login
    login.login("standard_user", "secret_sauce")

    # Add two products
    inventory.add_first_product()
    inventory.add_first_product()  # add first product again for demo

    # Open cart
    cart.open_cart()

    # Get cart items
    items = cart.get_cart_items()

    # Check if cart has at least 1 item
    assert len(items) >= 1

def test_remove_item_updates_cart(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    # Login and add product
    login.login("standard_user", "secret_sauce")
    inventory.add_first_product()

    cart.open_cart()

    # Remove the product
    first_item = cart.get_cart_items()[0]
    cart.remove_item(first_item)

    # Cart should be empty
    assert len(cart.get_cart_items()) == 0

def test_proceed_to_checkout(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    # Login and add product
    login.login("standard_user", "secret_sauce")
    inventory.add_first_product()

    # Open cart and proceed to checkout
    cart.open_cart()
    cart.proceed_to_checkout()

    # Assert URL contains checkout-step-one.html
    assert "checkout-step-one.html" in page.url