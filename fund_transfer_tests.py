from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import traceback

# Initialize the WebDriver (Ensure you've set up the appropriate WebDriver path)
driver = webdriver.Chrome()
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
    driver.get("https://www.demo.guru99.com/V4/manager/FundTransInput.php")


# Run login
login("mngr595557", "sApEgad")

# List to track test results
test_results = []


# Utility function for error message checks
def check_error_message(element_id, expected_message):
    message_element = driver.find_element(By.ID, element_id)
    assert message_element.text == expected_message, f"Expected '{expected_message}', but got '{message_element.text}'"


# Function to run each test case
def run_test(test_func):
    try:
        test_func()
        test_results.append((test_func.__name__, "PASS"))
    except AssertionError as e:
        test_results.append((test_func.__name__, "FAIL", str(e)))
    except Exception:
        test_results.append((test_func.__name__, "ERROR", traceback.format_exc()))


# Fund Transfer Test Cases
def test_verify_payers_account_number_not_empty():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.clear()  # Leave it blank
    payers_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message10", "Payers Account Number must not be blank")


def test_special_characters_not_allowed_in_payers_account():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.clear()
    payers_account_field.send_keys("!@#$%^&*()")  # Enter special characters
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message10", "Special characters are not allowed")


def test_alphabetic_characters_not_allowed_in_payers_account():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.clear()
    payers_account_field.send_keys("abcdef")  # Enter alphabet characters
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message10", "Characters are not allowed")


def test_verify_payees_account_number_not_empty():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.clear()  # Leave it blank
    payees_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message11", "Payees Account Number must not be blank")


def test_special_characters_not_allowed_in_payees_account():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.clear()
    payees_account_field.send_keys("!@#$%^&*()")  # Enter special characters
    payees_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message11", "Special characters are not allowed")


def test_alphabetic_characters_not_allowed_in_payees_account():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.clear()
    payees_account_field.send_keys("abcdef")  # Enter alphabet characters
    payees_account_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message11", "Characters are not allowed")


def test_verify_amount_not_empty():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys("139425")  # Valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()  # Leave Amount blank
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Amount field must not be blank")


def test_special_characters_not_allowed_in_amount():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys("139425")  # Valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("!@#$%")  # Enter special characters
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Special characters are not allowed")


def test_alphabetic_characters_not_allowed_in_amount():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys("139425")  # Valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("abc")  # Enter alphabet characters
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Characters are not allowed")


def test_verify_description_not_empty():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys("139425")  # Valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("100")  # Valid Amount
    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()  # Leave Description blank
    description_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message17", "Description can not be blank")


def test_invalid_transfer_amount():
    driver.get("https://www.demo.guru99.com/V4/manager/FundTransInput.php")
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("139424")  # Valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.send_keys("139425")  # Valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("999999")  # Enter an invalid transfer amount
    description_field = driver.find_element(By.NAME, "desc")
    description_field.send_keys("Test transfer")  # Valid Description
    driver.find_element(By.NAME, "AccSubmit").click()  # Click Submit

    # Check if the expected error message appears
    try:
        # Wait for the alert to be present
        WebDriverWait(driver, 10).until(ec.alert_is_present())
        alert = driver.switch_to.alert  # Switch to the alert
        assert alert.text == "Transfer Failed. Account Balance low!!", f"Expected alert message: 'Transfer Failed. Account Balance low!!', but got: '{alert.text}'"
        alert.accept()  # Accept the alert to close it
    except Exception:
        assert False, "Expected alert not displayed."


def test_successful_fund_transfer():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.clear()
    payers_account_field.send_keys("139424")  # Enter valid Payers Account
    payees_account_field = driver.find_element(By.NAME, "payeeaccount")
    payees_account_field.clear()
    payees_account_field.send_keys("139425")  # Enter valid Payees Account
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("1")  # Enter valid Amount
    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()
    description_field.send_keys("Transfer Test")  # Enter valid Description
    driver.find_element(By.NAME, "AccSubmit").click()  # Click Submit

    # Check for the successful transfer message (adjust according to your application)
    success_message_element = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Fund Transfer Details')]"))
    )
    assert success_message_element is not None, "Expected success message for fund transfer not displayed."


# Running all test cases
test_cases = [
    test_verify_payers_account_number_not_empty,
    test_special_characters_not_allowed_in_payers_account,
    test_alphabetic_characters_not_allowed_in_payers_account,
    test_verify_payees_account_number_not_empty,
    test_special_characters_not_allowed_in_payees_account,
    test_alphabetic_characters_not_allowed_in_payees_account,
    test_verify_amount_not_empty,
    test_special_characters_not_allowed_in_amount,
    test_alphabetic_characters_not_allowed_in_amount,
    test_verify_description_not_empty,
    test_successful_fund_transfer,
    test_invalid_transfer_amount
]

for test_case in test_cases:
    run_test(test_case)

# Print test results
print("Test Results:")
for result in test_results:
    print(result)

# Close the driver
driver.quit()
