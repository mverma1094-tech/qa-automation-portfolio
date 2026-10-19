# Bug Report Example

Saucedemo includes a `problem_user` account with intentional defects, which makes it a good place to practice bug reporting.

---

**Bug ID:** BUG-001
**Title:** Product images all show the same picture when logged in as problem_user
**Environment:** Chrome (latest), Windows 11, https://www.saucedemo.com
**Severity:** Medium | **Priority:** Medium

**Steps to Reproduce**
1. Go to https://www.saucedemo.com
2. Log in with `problem_user` / `secret_sauce`
3. Look at the product images on the Products page

**Expected Result:** Each product shows its own image.
**Actual Result:** Every product shows the same dog image.

**Attachments:** screenshot of the Products page
**Notes:** Does not happen with `standard_user`, so the issue is tied to this account's data, not the page layout.

---

**Bug ID:** BUG-002
**Title:** Last Name field does not keep typed text on checkout (problem_user)
**Environment:** Chrome (latest), Windows 11
**Severity:** High (blocks checkout) | **Priority:** High

**Steps to Reproduce**
1. Log in as `problem_user` / `secret_sauce`
2. Add any item to the cart and click Checkout
3. Type "Test" in First Name, then type "User" in Last Name

**Expected Result:** Each field keeps its own text.
**Actual Result:** Typing in Last Name changes the First Name field instead, and Last Name stays empty, so checkout cannot continue.
