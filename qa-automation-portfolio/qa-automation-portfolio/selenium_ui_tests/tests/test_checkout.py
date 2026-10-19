import pytest
from pages.checkout_page import CheckoutPage


def test_full_checkout_succeeds(logged_in, driver):
    logged_in.add_to_cart("sauce-labs-bike-light")
    logged_in.go_to_cart()
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_info("Test", "User", "20151")
    checkout.finish()
    assert checkout.confirmation_text() == "Thank you for your order!"


# Each required field left blank should block checkout with its own message
@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "User", "20151", "First Name is required"),
        ("Test", "", "20151", "Last Name is required"),
        ("Test", "User", "", "Postal Code is required"),
    ],
)
def test_checkout_requires_all_fields(logged_in, driver, first, last, postal, expected_error):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.go_to_cart()
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.fill_info(first, last, postal)
    assert expected_error in checkout.error_text()
