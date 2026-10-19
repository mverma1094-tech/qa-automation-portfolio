-- Test data. Most rows are clean. A few defects are planted on purpose
-- so the validation queries have something to catch (marked with -- DEFECT).

INSERT INTO customers VALUES
    (1, 'Ana',   'Lopez',  'ana.lopez@example.com'),
    (2, 'Ben',   'Carter', 'ben.carter@example.com'),
    (3, 'Chloe', 'Nguyen', 'chloe.nguyen@example.com'),
    (4, 'David', 'Kim',    'ben.carter@example.com'),   -- DEFECT: duplicate email
    (5, 'Ella',  'Brown',  NULL);                       -- DEFECT: missing email

INSERT INTO products VALUES
    (101, 'Wireless Earbuds', 59.99),
    (102, 'Phone Case',       19.99),
    (103, 'USB-C Charger',    24.99),
    (104, 'Screen Protector', -9.99);                   -- DEFECT: negative price

INSERT INTO orders VALUES
    (1001, 1,  '2026-10-01', 79.98),
    (1002, 2,  '2026-10-02', 24.99),
    (1003, 3,  '2026-10-03', 49.98),                    -- DEFECT: total should be 39.98
    (1004, 99, '2026-10-04', 19.99),                    -- DEFECT: customer 99 does not exist
    (1005, 1,  '2026-10-05', 59.99);

INSERT INTO order_items VALUES
    (1, 1001, 101, 1, 59.99),
    (2, 1001, 102, 1, 19.99),
    (3, 1002, 103, 1, 24.99),
    (4, 1003, 102, 2, 19.99),
    (5, 1004, 102, 1, 19.99),
    (6, 1005, 101, 1, 59.99),
    (7, 1005, 103, 0, 24.99);                           -- DEFECT: quantity of 0
