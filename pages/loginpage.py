from utils.config import BASE_URL

class Login:

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("input[name='user-name']")
        self.password_field = page.locator("input[name='password']")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def login(self, username, password):
        # Go to the login page
        self.page.goto(BASE_URL)

        # Wait for fields to appear before filling
        self.username_field.wait_for(state="visible")
        self.username_field.fill(username)

        self.password_field.wait_for(state="visible")
        self.password_field.fill(password)

        # Click login
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.text_content()