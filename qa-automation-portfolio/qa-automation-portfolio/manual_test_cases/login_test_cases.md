# Manual Test Cases: Login and Checkout (saucedemo.com)

**Application:** https://www.saucedemo.com
**Techniques used:** Equivalence partitioning (EP), boundary value analysis (BVA), exploratory testing

## Login

| ID | Title | Technique | Steps | Test Data | Expected Result |
|----|-------|-----------|-------|-----------|-----------------|
| TC-01 | Valid login | EP (valid) | Enter username and password, click Login | standard_user / secret_sauce | Products page opens |
| TC-02 | Locked-out user | EP (invalid) | Enter credentials, click Login | locked_out_user / secret_sauce | Error: user has been locked out |
| TC-03 | Blank username | EP (invalid) | Leave username blank, enter password, click Login | "" / secret_sauce | Error: Username is required |
| TC-04 | Blank password | EP (invalid) | Enter username, leave password blank, click Login | standard_user / "" | Error: Password is required |
| TC-05 | Wrong password | EP (invalid) | Enter valid username, wrong password | standard_user / wrong123 | Error: username and password do not match |
| TC-06 | Username case sensitivity | EP (invalid) | Enter username in uppercase | STANDARD_USER / secret_sauce | Login fails with mismatch error |
| TC-07 | Leading/trailing spaces | Exploratory | Add a space before the username | " standard_user" / secret_sauce | Login fails, no crash |
| TC-08 | Very long input | BVA (upper edge) | Paste 256+ characters into username | 256 x "a" | Field handles input, error shown, no crash |

## Checkout: Information Step

| ID | Title | Technique | Steps | Test Data | Expected Result |
|----|-------|-----------|-------|-----------|-----------------|
| TC-09 | All fields valid | EP (valid) | Add item, go to checkout, fill all fields, Continue | Test / User / 20151 | Overview page opens |
| TC-10 | First name blank | EP (invalid) | Leave first name blank, Continue | "" / User / 20151 | Error: First Name is required |
| TC-11 | Last name blank | EP (invalid) | Leave last name blank, Continue | Test / "" / 20151 | Error: Last Name is required |
| TC-12 | Postal code blank | EP (invalid) | Leave postal code blank, Continue | Test / User / "" | Error: Postal Code is required |
| TC-13 | Postal code letters | Exploratory | Enter letters in postal code | Test / User / ABCDE | Note behavior (accepts any text: logged as observation) |
| TC-14 | Order total math | Exploratory | Add 2 items, check overview | Backpack + Bike Light | Item total = sum of prices, tax and total shown correctly |

## Cart

| ID | Title | Technique | Steps | Expected Result |
|----|-------|-----------|-------|-----------------|
| TC-15 | Add one item | EP (valid) | Click Add to cart on one item | Cart badge shows 1 |
| TC-16 | Remove item | EP (valid) | Add item, then click Remove | Cart badge disappears |
| TC-17 | Add all items | BVA (max) | Add all 6 products | Cart badge shows 6 |
| TC-18 | Cart after logout | Exploratory | Add item, log out, log back in | Note whether cart is kept (document behavior) |

**Automated:** TC-01 to TC-05, TC-09 to TC-12, TC-15, TC-16 are automated in `selenium_ui_tests/`.
