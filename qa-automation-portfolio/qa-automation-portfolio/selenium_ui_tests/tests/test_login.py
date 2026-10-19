import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login_opens_inventory(driver):
    LoginPage(driver).load().login("standard_user", "secret_sauce")
    assert InventoryPage(driver).title() == "Products"


def test_locked_out_user_sees_error(driver):
    page = LoginPage(driver).load()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.error_text()


# Equivalence partitioning: one test per class of invalid input
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("standard_user", "wrong_password", "do not match"),
        ("unknown_user", "secret_sauce", "do not match"),
    ],
)
def test_invalid_login_shows_error(driver, username, password, expected_error):
    page = LoginPage(driver).load()
    page.login(username, password)
    assert expected_error in page.error_text()
