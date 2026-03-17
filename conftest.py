# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=50)  # slow_mo helps visual verification
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         context.close()
#         browser.close()
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()