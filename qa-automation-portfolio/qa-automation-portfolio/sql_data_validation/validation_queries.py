"""
SQL data-validation checks.

Each query returns the rows that BREAK a business rule.
An empty result means the data passes that check.
"""

CHECKS = {
    "orders_with_unknown_customer": """
        SELECT o.order_id, o.customer_id
        FROM orders o
        LEFT JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """,

    "order_total_mismatch": """
        SELECT o.order_id,
               o.order_total,
               ROUND(SUM(oi.quantity * oi.unit_price), 2) AS calculated_total
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY o.order_id, o.order_total
        HAVING ROUND(SUM(oi.quantity * oi.unit_price), 2) <> o.order_total;
    """,

    "duplicate_customer_emails": """
        SELECT email, COUNT(*) AS times_used
        FROM customers
        WHERE email IS NOT NULL
        GROUP BY email
        HAVING COUNT(*) > 1;
    """,

    "customers_missing_email": """
        SELECT customer_id, first_name, last_name
        FROM customers
        WHERE email IS NULL OR TRIM(email) = '';
    """,

    "products_with_invalid_price": """
        SELECT product_id, name, price
        FROM products
        WHERE price <= 0;
    """,

    "order_items_with_invalid_quantity": """
        SELECT oi.item_id, oi.order_id, p.name, oi.quantity
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        WHERE oi.quantity <= 0;
    """,

    "item_price_differs_from_catalog": """
        SELECT oi.item_id, p.name, oi.unit_price, p.price AS catalog_price
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        WHERE oi.unit_price <> p.price;
    """,
}
