# QA Automation Portfolio

Manual and automated testing projects covering **UI automation, SQL data validation, security log analysis, and test case design**.

**Tools:** Python, Selenium WebDriver, PyTest, SQL (SQLite), Regex, GitHub Actions


---

## Projects

### 1. Selenium UI Test Suite — `selenium_ui_tests/`
Automated end-to-end tests for the [Sauce Demo](https://www.saucedemo.com) store, a public site built for testing practice.

- **15 automated tests** covering login, cart, product sorting, and checkout
- **Page Object Model**: locators and page actions live in `pages/`, separate from test logic
- **PyTest fixtures** handle browser setup/teardown and a reusable logged-in state
- **Parametrized tests** apply equivalence partitioning to invalid logins and required checkout fields
- **Explicit waits** instead of `sleep()` to keep tests stable

### 2. SQL Data Validation — `sql_data_validation/`
SQL checks that find bad data in a small retail/POS database (customers, products, orders, order items).

- **7 validation queries** using `JOIN`, `LEFT JOIN`, `WHERE`, `GROUP BY`, and `HAVING`
- Catches orphaned orders, order totals that don't match their line items, duplicate emails, missing data, negative prices, and zero quantities
- Test data includes **6 planted defects**; PyTest confirms each query catches its defect with no false positives
- `run_report.py` prints a pass/fail report

### 3. Security Log Parser — `log_parser/`
Python script that reads a Linux SSH auth log and flags suspicious activity using regex.

- Detects **brute-force attempts**, **username guessing**, and **successful logins after a brute-force attack**
- **8 PyTest tests**, including boundary value tests on the alert threshold (4 failures = no alert, 5 = alert)

### 4. Manual Test Cases — `manual_test_cases/`
- **18 test cases** for login, cart, and checkout, labeled by technique (equivalence partitioning, boundary value analysis, exploratory)
- **Bug report examples** written in a standard defect format (steps, expected vs. actual, severity, priority)

---

## How to Run

```bash
pip install -r requirements.txt

# SQL validation
cd sql_data_validation
pytest -v
python run_report.py

# Log parser
cd ../log_parser
pytest -v
python log_parser.py sample_auth.log

# Selenium (needs Google Chrome installed)
cd ../selenium_ui_tests
pytest -v
# To watch the browser:  HEADLESS=0 pytest -v
```

All tests also run automatically on every push through **GitHub Actions** (`.github/workflows/tests.yml`).
