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
    driver.get("https://www.demo.guru99.com/V4/manager/DepositInput.php")


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


def test_amount_blank():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys(Keys.TAB)
    check_error_message("message1", "Amount field must not be blank")


def test_amount_special_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("@#$%")
    amount_field.send_keys(Keys.TAB)
    check_error_message("message1", "Special characters are not allowed")


def test_amount_alphabets():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.clear()
    amount_field.send_keys("ABC123")
    amount_field.send_keys(Keys.TAB)
    check_error_message("message1", "Characters are not allowed")


def test_description_blank():
    description_field = driver.find_element(By.NAME, "desc")
    description_field.clear()
    description_field.send_keys(Keys.TAB)
    check_error_message("message17", "Description can not be blank")


def test_valid_deposit_submission():
    account_field = driver.find_element(By.NAME, "accountno")
    amount_field = driver.find_element(By.NAME, "ammount")
    description_field = driver.find_element(By.NAME, "desc")

    account_field.clear()
    amount_field.clear()
    description_field.clear()

    account_field.send_keys("139424")
    amount_field.send_keys("1")
    description_field.send_keys("gg")
    driver.find_element(By.NAME, "AccSubmit").click()

    WebDriverWait(driver, 2).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Transaction details of Deposit for Account"
        )
    )
    print("Success: Deposit submission success message displayed.")


# Running each test and storing results
for test in [
    test_account_number_blank,
    test_account_number_special_characters,
    test_account_number_alphabets,
    test_amount_blank,
    test_amount_special_characters,
    test_amount_alphabets,
    test_description_blank,
    test_valid_deposit_submission
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
