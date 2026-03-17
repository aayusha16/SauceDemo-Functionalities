class CartPage:
    def __init__(self, page):
        self.page = page
        # Elements
        self.cart_items = page.locator(".cart_item")
        self.checkout_btn = page.locator("#checkout")
        self.remove_buttons = page.locator(".cart_button")
        self.cart_icon = page.locator(".shopping_cart_link")  # to open cart

    # Open the cart page
    def open_cart(self):
        self.cart_icon.click()

    # Get list of product names in cart
    def get_cart_items(self):
        items = []
        for i in range(self.cart_items.count()):
            name = self.cart_items.nth(i).locator(".inventory_item_name").text_content()
            items.append(name)
        return items

    # Remove a specific item by name
    def remove_item(self, item_name):
        for i in range(self.cart_items.count()):
            name = self.cart_items.nth(i).locator(".inventory_item_name").text_content()
            if name == item_name:
                self.cart_items.nth(i).locator(".cart_button").click()
                break

    # Proceed to checkout
    def proceed_to_checkout(self):
        self.checkout_btn.click()