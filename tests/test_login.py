import pytest
from pages.loginpage import Login


@pytest.mark.login
def test_valid_login(page):
    login = Login(page)
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url


@pytest.mark.login
def test_locked_out_user(page):
    login = Login(page)
    login.login("locked_out_user", "secret_sauce")
    assert "inventory.html" not in page.url
    assert "locked out" in login.get_error_message().lower()


@pytest.mark.login
def test_invalid_username(page):
    login = Login(page)
    login.login("wrong_user", "secret_sauce")
    assert "inventory.html" not in page.url
    assert login.get_error_message() is not None


@pytest.mark.login
def test_invalid_password(page):
    login = Login(page)
    login.login("standard_user", "wrong_pass")
    assert "inventory.html" not in page.url
    assert login.get_error_message() is not None


@pytest.mark.login
def test_blank_username_password(page):
    login = Login(page)
    login.login("", "")
    assert login.get_error_message() is not None


@pytest.mark.login
def test_username_with_spaces(page):
    login = Login(page)
    login.login(" standard_user ", "secret_sauce")
    assert "inventory.html" not in page.url


@pytest.mark.login
def test_username_case_sensitive(page):
    login = Login(page)
    login.login("STANDARD_USER", "secret_sauce")
    assert "inventory.html" not in page.url


@pytest.mark.login
def test_only_username(page):
    login = Login(page)
    login.login("standard_user", "")
    assert login.get_error_message() is not None