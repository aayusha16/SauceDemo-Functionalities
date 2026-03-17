class AddCartPage:
    def __init__(self, page):
        self.page = page
        # Cart page
        self.cart_btn = page.locator("shopping_cart_container")   # Cart icon button
        self.checkout_btn = page.locator("checkout")         # Checkout button on cart page

        # Checkout: Your Info
        self.first_name_input = page.locator("first-name")
        self.last_name_input = page.locator("last-name")
        self.postal_code_input = page.locator("postal-code")
        self.continue_btn = page.locator("continue")
        self.error_msg = page.locator("h3[data-test='error']")  # Error message element

    # Click cart button
    def open_cart(self):
        self.cart_btn.click()

    # Click checkout button from cart
    def click_checkout(self):
        self.checkout_btn.click()

    # Fill customer info (we’ll fill selectively in tests)
    def fill_first_name_only(self, first_name):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill("")        # leave blank
        self.postal_code_input.fill("")      # leave blank

    # Click continue on checkout page
    def click_continue(self):
        self.continue_btn.click()

    # Get error message if validation fails
    def get_error_message(self):
        return self.error_msg.text_content()