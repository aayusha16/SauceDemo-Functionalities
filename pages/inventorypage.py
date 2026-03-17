class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.first_product_name = page.locator(".inventory_item_name").first
        self.add_to_cart_buttons = page.locator(".btn_inventory")  # better selector for SauceDemo
        self.cart_badge = page.locator(".shopping_cart_badge")

    # Product actions
    def open_first_product(self):
        self.first_product_name.click()

    def add_first_product(self):
        self.add_to_cart_buttons.first.click()

    def remove_first_product(self):
        self.add_to_cart_buttons.first.click()  # button changes to "Remove"

    # Helper to get cart count
    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.text_content())