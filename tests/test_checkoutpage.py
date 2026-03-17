from pages.loginpage import Login
from pages.inventorypage import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_success(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Login
    login.login("standard_user", "secret_sauce")

    # Add first product
    inventory.add_first_product()

    # Open cart and proceed to checkout
    cart.open_cart()
    cart.proceed_to_checkout()

    # Fill all details correctly
    checkout.fill_checkout_info(first_name="Aayusha", last_name="Bisunke", postal_code="44600")
    checkout.click_continue()
    checkout.click_finish()

    # Assert order completed page appears
    assert "checkout-complete.html" in page.url

def test_checkout_missing_fields(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Login
    login.login("standard_user", "secret_sauce")

    # Add first product
    inventory.add_first_product()

    # Open cart and proceed to checkout
    cart.open_cart()
    cart.proceed_to_checkout()

    # Fill only first name (leave last name & postal code blank)
    checkout.fill_checkout_info(first_name="Aayusha")
    checkout.click_continue()

    # Assert error message is shown
    assert "Error" in checkout.get_error_message()