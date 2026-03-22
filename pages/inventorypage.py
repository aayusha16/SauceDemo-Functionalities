from playwright.sync_api import Page

class Inventory:
    def __init__(self, page: Page):
        self.page = page

    # Get list of all product names
    def get_product_list(self):
        product_elements = self.page.locator(".inventory_item_name")
        return [el.inner_text() for el in product_elements.all()]

    # Add a product to cart by name
    def add_to_cart(self, product_name):
        # Locate the "Add to cart" button for the product dynamically
        add_button = self.page.locator(f"div.inventory_item:has-text('{product_name}') button")
        add_button.click()

    # Remove a product from cart by name
    def remove_from_cart(self, product_name):
        remove_button = self.page.locator(f"div.inventory_item:has-text('{product_name}') button:has-text('Remove')")
        remove_button.click()

    # Get cart count
    def get_cart_count(self):
        cart_badge = self.page.locator(".shopping_cart_badge")
        if cart_badge.count() == 0:
            return 0
        return int(cart_badge.inner_text())

    # Go to cart page
    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()