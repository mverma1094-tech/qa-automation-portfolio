from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def title(self):
        return self.text_of(self.TITLE)

    def item_count(self):
        self.find(self.ITEMS)
        return len(self.driver.find_elements(*self.ITEMS))

    def add_to_cart(self, product_slug):
        # e.g. "sauce-labs-backpack" -> button id "add-to-cart-sauce-labs-backpack"
        self.click((By.ID, f"add-to-cart-{product_slug}"))

    def remove_from_cart(self, product_slug):
        self.click((By.ID, f"remove-{product_slug}"))

    def cart_count(self):
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def sort_by(self, value):
        # values: "az", "za", "lohi", "hilo"
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(value)

    def prices(self):
        self.find(self.ITEM_PRICES)
        return [float(p.text.replace("$", "")) for p in self.driver.find_elements(*self.ITEM_PRICES)]

    def go_to_cart(self):
        self.click(self.CART_LINK)
