import pytest
from playwright.sync_api import sync_playwright
from pages.loginpage import Login
import logging

# ---------- Logging Setup ----------
logging.basicConfig(
    filename="test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()

# ---------- Fixtures ----------

@pytest.fixture(scope="session")
def browser():
    """Launch a single browser session for all tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fresh page for login tests (not logged in)."""
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()


@pytest.fixture
def logged_in_page(browser):
    """Fresh page that is already logged in."""
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    login = Login(page)
    login.login("standard_user", "secret_sauce")
    yield page
    context.close()



def pytest_configure(config):
    config.addinivalue_line("markers", "login: mark test as login test")
    config.addinivalue_line("markers", "inventory: mark test as inventory test")
    config.addinivalue_line("markers", "cart: mark test as cart test")