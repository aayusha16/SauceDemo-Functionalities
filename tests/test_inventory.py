def test_add_product_to_cart(page):
    Login = Login(page)
    inventory = InventoryPage(page)

    Login.login("standard_user", "secret_sauce")
    inventory.add_first_product()

    assert inventory.get_cart_count() == 1