class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.first_product_name = page.locator(".inventory_item_name ").first
        self.add_to_cart_buttons = page.locator(".add-to-cart")
        self.cart_badge = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_names = page.locator(".inventory_item_name ")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_images = page.locator(".inventory_item_img")

    # Product actions
    def open_first_product(self):
        self.first_product_name.click()

    def add_first_product(self):
        self.add_to_cart_buttons.first.click()

    def remove_first_product(self):
        self.add_to_cart_buttons.first.click()  # button changes to "Remove"

    # Sorting
    def sort_products(self, option):
        self.sort_dropdown.select_option(option)

    # Helpers
    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.text_content())

    def get_all_prices(self):
        prices = []
        for i in range(self.product_prices.count()):
            text = self.product_prices.nth(i).text_content().replace("$","")
            prices.append(float(text))
        return prices

    def are_products_visible(self):
        return (
            self.product_names.count() > 0 and
            self.product_prices.count() > 0 and
            self.product_images.count() > 0
        )