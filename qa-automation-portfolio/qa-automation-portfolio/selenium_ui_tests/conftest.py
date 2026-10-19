import os
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    """Start Chrome before each test and close it afterward."""
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    """Log in as the standard user and return the inventory page."""
    LoginPage(driver).load().login("standard_user", "secret_sauce")
    return InventoryPage(driver)
