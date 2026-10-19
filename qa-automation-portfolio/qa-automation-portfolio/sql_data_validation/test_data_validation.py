"""
These tests prove each SQL check catches exactly the defect planted in seed_data.sql,
and does not flag any clean rows (no false positives).
"""
import pytest
from db import build_database, run_check
from validation_queries import CHECKS


@pytest.fixture(scope="module")
def conn():
    connection = build_database()
    yield connection
    connection.close()


def test_finds_order_with_unknown_customer(conn):
    rows = run_check(conn, CHECKS["orders_with_unknown_customer"])
    assert rows == [(1004, 99)]


def test_finds_order_total_mismatch(conn):
    rows = run_check(conn, CHECKS["order_total_mismatch"])
    assert [r[0] for r in rows] == [1003]


def test_finds_duplicate_email(conn):
    rows = run_check(conn, CHECKS["duplicate_customer_emails"])
    assert rows == [("ben.carter@example.com", 2)]


def test_finds_customer_missing_email(conn):
    rows = run_check(conn, CHECKS["customers_missing_email"])
    assert [r[0] for r in rows] == [5]


def test_finds_negative_price(conn):
    rows = run_check(conn, CHECKS["products_with_invalid_price"])
    assert [r[0] for r in rows] == [104]


def test_finds_zero_quantity(conn):
    rows = run_check(conn, CHECKS["order_items_with_invalid_quantity"])
    assert [r[0] for r in rows] == [7]


def test_item_prices_match_catalog(conn):
    # No price defect planted here, so this check should pass
    assert run_check(conn, CHECKS["item_price_differs_from_catalog"]) == []
