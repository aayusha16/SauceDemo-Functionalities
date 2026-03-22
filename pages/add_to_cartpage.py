from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def get_cart_products(self):
        """Return list of product names in the cart"""
        product_elements = self.page.locator(".cart_item .inventory_item_name")
        return [el.inner_text() for el in product_elements.all()]

    def remove_product(self, product_name):
        """Remove a specific product from the cart"""
        self.page.locator(f"div.cart_item:has-text('{product_name}') button").click()

    def continue_shopping(self):
        """Click Continue Shopping button to go back to inventory"""
        self.page.wait_for_selector("text=Continue Shopping")
        self.page.locator("text=Continue Shopping").click()

    def go_to_checkout(self):
        """Click 'Checkout' button to go to checkout page"""
        self.page.locator("text=Checkout").click()  # safer than class