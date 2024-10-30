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
    driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")


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
def test_customer_id_blank():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Customer ID is required")


def test_customer_id_special_characters():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys("@#$%")
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Special characters are not allowed")


def test_customer_id_alphabets():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys("ABC123")
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Characters are not allowed")


def test_initial_deposit_blank():
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Initial Deposit must not be blank")


def test_initial_deposit_special_characters():
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys("@#$%")
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Special characters are not allowed")


def test_initial_deposit_alphabets():
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys("DepositABC")
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Characters are not allowed")


def test_initial_deposit_below_minimum():
    driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")
    customer_id_field = driver.find_element(By.NAME, "cusid")
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")

    customer_id_field.clear()
    customer_id_field.send_keys("47674")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys("5")
    driver.find_element(By.NAME, "button2").click()

    # Check if alert is displayed for minimum deposit
    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    assert alert.text == "Initial deposit must be 500 or more", f"Expected alert message not found. Got '{alert.text}'"
    alert.accept()
    print("Success: Minimum deposit alert displayed.")


def test_valid_account_creation():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")

    customer_id_field.clear()
    initial_deposit_field.clear()

    customer_id_field.send_keys("47674")
    initial_deposit_field.send_keys("5000")
    driver.find_element(By.NAME, "button2").click()

    # Wait for success message and account detail table
    try:
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "heading3"))
        )
        success_elements = driver.find_elements(By.CLASS_NAME, "heading3")
        success_message_found = any("Account Generated Successfully!!!" in element.text for element in success_elements)
        assert success_message_found, "Success message not found in any 'heading3' element."
        print("Success: Account creation success message displayed.")
    except Exception as e:
        print(f"Failure: {str(e)}")


# Running each test and storing results
for test in [
    test_customer_id_blank,
    test_customer_id_special_characters,
    test_customer_id_alphabets,
    test_initial_deposit_blank,
    test_initial_deposit_special_characters,
    test_initial_deposit_alphabets,
    test_valid_account_creation,
    test_initial_deposit_below_minimum,
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
