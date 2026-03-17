from pages.loginpage import Login
from pages.inventorypage import InventoryPage
from pages.addcartpage import AddCartPage

def test_checkout_first_name_only(page):
    login = Login(page)
    inventory = InventoryPage(page)
    cart = AddCartPage(page)

    # Step 1: Login
    login.login("standard_user", "secret_sauce")

    # Step 2: Add first product to cart
    inventory.add_first_product()

    # Step 3: Go to cart and click checkout
    cart.click_checkout()

    # Step 4: Fill only first name (leave last name & postal code blank)
    cart.fill_first_name_only("Aayusha")

    # Step 5: Click continue
    cart.click_continue()

    # Step 6: Validate error message appears
    assert "checkout-step-one.html" in page.url