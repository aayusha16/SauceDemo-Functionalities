# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.loginpage import Login

@pytest.fixture
def logged_in_page():
    """
    Creates a fresh browser & context for each test,
    logs in, yields the page, and closes everything after the test.
    """
    with sync_playwright() as p:
        # Launch a new browser per test
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()

        # Go to login page
        page.goto("https://www.saucedemo.com/")

        # Perform login
        login = Login(page)
        login.login("standard_user", "secret_sauce")

        # Yield the page to the test
        yield page

        # Cleanup after test
        context.close()
        browser.close()