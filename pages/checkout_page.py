class CheckoutPage:
    def __init__(self, page):
        self.page = page

        # Elements
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.error_msg = page.locator("h3[data-test='error']")

    # Fill checkout info
    def fill_checkout_info(self, first_name="", last_name="", postal_code=""):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    # Click continue
    def click_continue(self):
        self.continue_btn.click()

    # Click finish
    def click_finish(self):
        self.finish_btn.click()

    # Get error message
    def get_error_message(self):
        return self.error_msg.text_content()