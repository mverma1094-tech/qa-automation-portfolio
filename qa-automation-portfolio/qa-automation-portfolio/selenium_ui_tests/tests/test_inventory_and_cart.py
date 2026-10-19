def test_inventory_shows_six_products(logged_in):
    assert logged_in.item_count() == 6


def test_add_item_updates_cart_badge(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    assert logged_in.cart_count() == 1


def test_add_then_remove_item_clears_cart(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.remove_from_cart("sauce-labs-backpack")
    assert logged_in.cart_count() == 0


def test_sort_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.prices()
    assert prices == sorted(prices)


def test_sort_price_high_to_low(logged_in):
    logged_in.sort_by("hilo")
    prices = logged_in.prices()
    assert prices == sorted(prices, reverse=True)
