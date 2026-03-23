import pytest
import logging
from pages.loginpage import Login

logger = logging.getLogger(__name__)


# -------------------- TESTS --------------------

@pytest.mark.login
def test_valid_login(page):
    logger.info("Running test_valid_login")

    login = Login(page)

    logger.info("Logging in with valid credentials")
    login.login("standard_user", "secret_sauce")

    page.wait_for_url("**/inventory.html")

    assert "inventory.html" in page.url

    logger.info("Test passed: Valid login successful")


@pytest.mark.login
def test_locked_out_user(page):
    logger.info("Running test_locked_out_user")

    login = Login(page)

    logger.info("Attempting login with locked out user")
    login.login("locked_out_user", "secret_sauce")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Locked out user blocked")


@pytest.mark.login
def test_invalid_username(page):
    logger.info("Running test_invalid_username")

    login = Login(page)

    logger.info("Attempting login with invalid username")
    login.login("wrong_user", "secret_sauce")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Invalid username handled")


@pytest.mark.login
def test_invalid_password(page):
    logger.info("Running test_invalid_password")

    login = Login(page)

    logger.info("Attempting login with invalid password")
    login.login("standard_user", "wrong_pass")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Invalid password handled")


@pytest.mark.login
def test_blank_username_password(page):
    logger.info("Running test_blank_username_password")

    login = Login(page)

    logger.info("Attempting login with blank credentials")
    login.login("", "")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Blank credentials handled")


@pytest.mark.login
def test_username_with_spaces(page):
    logger.info("Running test_username_with_spaces")

    login = Login(page)

    logger.info("Attempting login with username containing spaces")
    login.login(" standard_user ", "secret_sauce")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Username with spaces handled")


@pytest.mark.login
def test_username_case_sensitive(page):
    logger.info("Running test_username_case_sensitive")

    login = Login(page)

    logger.info("Attempting login with uppercase username")
    login.login("STANDARD_USER", "secret_sauce")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Case sensitivity verified")


@pytest.mark.login
def test_only_username(page):
    logger.info("Running test_only_username")

    login = Login(page)

    logger.info("Attempting login with only username")
    login.login("standard_user", "")

    error = login.get_error_message()
    logger.info(f"Error message: {error}")

    assert error is not None

    logger.info("Test passed: Missing password handled")