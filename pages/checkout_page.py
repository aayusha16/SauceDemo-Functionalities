from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    # Fill in checkout information
    def enter_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)

    # Click Continue to go to overview page
    def continue_checkout(self):
        self.page.locator("#continue").click()

    # Click Cancel to return to cart
    def cancel_checkout(self):
        self.page.locator("#cancel").click()