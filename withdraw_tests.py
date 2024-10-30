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
    driver.get("https://www.demo.guru99.com/V4/manager/DepositInput.php")


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


# Withdrawal Test Cases
def test_verify_account_number_field_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()  # Leave it blank
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message2", "Account Number must not be blank")


def test_special_characters_not_allowed_in_account_number():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()
    account_no_field.send_keys("!@#$%^&*()")  # Enter special characters
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message2", "Special characters are not allowed")


def test_alphabetic_characters_not_allowed_in_account_number():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()
    account_no_field.send_keys("abcdef")  # Enter alphabet characters
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message2", "Characters are not allowed")


def test_verify_amount_field_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("123456")  # Valid Account No
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()  # Leave Amount blank
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Amount field must not be blank")


def test_special_characters_not_allowed_in_amount():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("123456")  # Valid Account No
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("!@#$%")  # Enter special characters
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Special characters are not allowed")


def test_alphabetic_characters_not_allowed_in_amount():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("123456")  # Valid Account No
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("abc")  # Enter alphabet characters
    amount_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message1", "Characters are not allowed")


def test_verify_description_field_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("123456")  # Valid Account No
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("100")  # Valid Amount
    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()  # Leave Description blank
    description_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message17", "Description can not be blank")


def test_successful_deposit_with_valid_values():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()
    account_no_field.send_keys("139424")  # Enter valid Account ID

    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("1")  # Enter valid Amount

    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()
    description_field.send_keys("gg")  # Enter valid Description

    driver.find_element(By.NAME, "AccSubmit").click()  # Click Submit

    try:
        # Check if the deposit was successful
        success_message_element = WebDriverWait(driver, 2).until(
            ec.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Transaction successful')]"))
        )
        assert success_message_element is not None, "Deposit was not successful."
        print("Success: Deposit was successful.")
    except Exception:
        raise AssertionError("Deposit submission failed: Success message not displayed.")



# Execute test cases
test_cases = [
    test_verify_account_number_field_not_blank,
    test_special_characters_not_allowed_in_account_number,
    test_alphabetic_characters_not_allowed_in_account_number,
    test_verify_amount_field_not_blank,
    test_special_characters_not_allowed_in_amount,
    test_alphabetic_characters_not_allowed_in_amount,
    test_verify_description_field_not_blank,
    test_successful_deposit_with_valid_values,
]

for test in test_cases:
    run_test(test)

# Print test results
for result in test_results:
    print(result)

# Close the driver
driver.quit()
