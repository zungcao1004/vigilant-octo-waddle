from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import traceback

# Initialize the WebDriver (Ensure you've set up the appropriate WebDriver path)
driver = webdriver.Chrome()

# Login page
driver.get("https://www.demo.guru99.com/V4/index.php")


# Login function
def login(username, password):
    username_field = driver.find_element(By.NAME, "uid")
    username_field.send_keys(username)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    driver.find_element(By.NAME, "btnLogin").click()
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Welcome To Manager's Page of Guru99 Bank"
        )
    )
    driver.get("https://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php")  # Replace with actual URL


# Run login
login("mngr595557", "sApEgad")


# Utility function for error message checks
def check_error_message(element_id, expected_message):
    message_element = driver.find_element(By.ID, element_id)
    assert message_element.text == expected_message, f"Expected '{expected_message}', but got '{message_element.text}'"


# List to track test results
test_results = []


# Function to run each test case
def run_test(test_func):
    try:
        test_func()
        test_results.append((test_func.__name__, "PASS"))
    except AssertionError as e:
        test_results.append((test_func.__name__, "FAIL", str(e)))
    except Exception:
        test_results.append((test_func.__name__, "ERROR", traceback.format_exc()))


# Test Cases
def test_account_number_blank():
    account_field = driver.find_element(By.NAME, "accountno")
    account_field.clear()
    account_field.send_keys(Keys.TAB)
    check_error_message("message2", "Account Number must not be blank")


def test_account_number_special_characters():
    account_field = driver.find_element(By.NAME, "accountno")
    account_field.clear()
    account_field.send_keys("@#$%")
    account_field.send_keys(Keys.TAB)
    check_error_message("message2", "Special characters are not allowed")


def test_account_number_alphabets():
    account_field = driver.find_element(By.NAME, "accountno")
    account_field.clear()
    account_field.send_keys("ABC123")
    account_field.send_keys(Keys.TAB)
    check_error_message("message2", "Characters are not allowed")


def test_from_date_blank():
    from_date_field = driver.find_element(By.NAME, "fdate")
    from_date_field.clear()
    from_date_field.send_keys(Keys.TAB)
    check_error_message("message26", "From Date Field must not be blank")


def test_to_date_blank():
    to_date_field = driver.find_element(By.NAME, "tdate")
    to_date_field.clear()
    to_date_field.send_keys(Keys.TAB)
    check_error_message("message27", "To Date Field must not be blank")


def test_minimum_transaction_value_special_characters():
    amount_field = driver.find_element(By.NAME, "amountlowerlimit")
    amount_field.clear()
    amount_field.send_keys("@#$%")  # Enter special characters
    amount_field.send_keys(Keys.TAB)
    check_error_message("message12", "Special characters are not allowed")  # Check error message


def test_minimum_transaction_value_alphabets():
    amount_field = driver.find_element(By.NAME, "amountlowerlimit")
    amount_field.clear()
    amount_field.send_keys("ABC123")  # Enter alphabet characters
    amount_field.send_keys(Keys.TAB)
    check_error_message("message12", "Characters are not allowed")  # Check error message


def test_number_of_transactions_special_characters():
    transaction_field = driver.find_element(By.NAME, "numtransaction")
    transaction_field.clear()
    transaction_field.send_keys("@#$%")  # Enter special characters
    transaction_field.send_keys(Keys.TAB)
    check_error_message("message13", "Special characters are not allowed")  # Check error message


def test_number_of_transactions_alphabets():
    transaction_field = driver.find_element(By.NAME, "numtransaction")
    transaction_field.clear()
    transaction_field.send_keys("ABC123")  # Enter alphabet characters
    transaction_field.send_keys(Keys.TAB)
    check_error_message("message13", "Characters are not allowed")  # Check error message


def test_validate_date_order():
    account_field = driver.find_element(By.NAME, "accountno")
    from_date_field = driver.find_element(By.NAME, "fdate")
    to_date_field = driver.find_element(By.NAME, "tdate")

    account_field.clear()
    account_field.send_keys("139424")  # Enter a valid account number

    from_date_field.clear()
    from_date_field.send_keys("2024-10-31")  # Enter From Date (invalid)

    to_date_field.clear()
    to_date_field.send_keys("2024-10-30")  # Enter To Date (invalid)

    to_date_field.send_keys(Keys.TAB)  # Move to next field
    try:
        alert = WebDriverWait(driver, 1).until(ec.alert_is_present())

        # Verify alert text if present
        if "invalid" in alert.text:
            print("Alert message verified: 'invalid From Date, To Date'")
        else:
            raise AssertionError("Expected alert with 'invalid From Date, To Date' not found")
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError("Failed to find alert or element")


def test_valid_submission():
    account_field = driver.find_element(By.NAME, "accountno")
    from_date_field = driver.find_element(By.NAME, "fdate")
    to_date_field = driver.find_element(By.NAME, "tdate")

    account_field.clear()
    account_field.send_keys("139424")

    from_date_field.clear()
    from_date_field.send_keys("2024-10-30")

    to_date_field.clear()
    to_date_field.send_keys("2024-10-30")

    driver.find_element(By.NAME, "AccSubmit").click()

    expected_url = "https://www.demo.guru99.com/V4/manager/CustomisedStatement.php"
    if driver.current_url != expected_url:
        raise AssertionError(f"Expected URL: {expected_url}, Actual URL: {driver.current_url}")
    page_body = driver.find_element(By.TAG_NAME, "body").text
    if "transactions" not in page_body.lower():
        raise AssertionError(f"Expected 'transactions' message in body, not found.")

    print("Success: Submission success message displayed.")


# Running each test and storing results
for test in [
    test_account_number_blank,
    test_account_number_special_characters,
    test_account_number_alphabets,
    test_from_date_blank,
    test_to_date_blank,
    test_minimum_transaction_value_special_characters,
    test_minimum_transaction_value_alphabets,
    test_number_of_transactions_special_characters,
    test_number_of_transactions_alphabets,
    test_validate_date_order,
    test_valid_submission
]:
    run_test(test)

# Print test results summary
print("\nTest Results:")
for result in test_results:
    if len(result) == 2:
        print(f"{result[0]}: {result[1]}")
    else:
        print(f"{result[0]}: {result[1]} - {result[2]}")

# Close the browser
driver.quit()
