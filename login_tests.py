from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import traceback

# Initialize the WebDriver (Ensure you've set up the appropriate WebDriver path)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://www.demo.guru99.com/V4/index.php")

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


# Login Test Cases
def test_validate_username_field():
    username_field = driver.find_element(By.NAME, "uid")
    username_field.clear()  # Leave Username blank
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("pass123")  # Enter Password
    username_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message23", "User-ID must not be blank")


def test_validate_password_field():
    username_field = driver.find_element(By.NAME, "uid")
    username_field.clear()
    username_field.send_keys("user123")  # Enter valid Username
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()  # Leave Password blank
    password_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error message
    check_error_message("message18", "Password must not be blank")


def test_leave_both_fields_blank():
    username_field = driver.find_element(By.NAME, "uid")
    username_field.clear()  # Leave Username blank
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()  # Leave Password blank
    password_field.send_keys(Keys.TAB)  # Move focus to trigger validation

    # Check for the expected error messages
    check_error_message("message23", "User-ID must not be blank")
    check_error_message("message18", "Password must not be blank")


def test_test_login_with_both_fields_blank():
    username_field = driver.find_element(By.NAME, "uid")
    username_field.clear()  # Leave Username blank
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()  # Leave Password blank
    driver.find_element(By.NAME, "btnLogin").click()  # Click Submit

    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    assert alert.text == "User or Password is not valid", f"Expected alert message not found. Got '{alert.text}'"
    alert.accept()


def test_successful_login_with_valid_credentials():
    username_field = driver.find_element(By.NAME, "uid")
    username_field.clear()
    username_field.send_keys("mngr595557")  # Enter valid Username
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("sApEgad")  # Enter valid Password
    driver.find_element(By.NAME, "btnLogin").click()  # Click Submit

    # Check if login was successful by verifying redirection to the dashboard
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Welcome To Manager's Page of Guru99 Bank"
        )
    )


# Execute test cases
test_cases = [
    test_validate_username_field,
    test_validate_password_field,
    test_leave_both_fields_blank,
    test_test_login_with_both_fields_blank,
    test_successful_login_with_valid_credentials,
]

for test in test_cases:
    run_test(test)

# Print test results
for result in test_results:
    print(result)

# Close the driver
driver.quit()
