import traceback

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Define a list to track test results
test_results = []

# Initialize the WebDriver (Ensure you've set up the appropriate WebDriver path)
driver = webdriver.Chrome()
# login page
driver.get("https://www.demo.guru99.com/V4/index.php")


def login(username, password):
    # Find and fill the username field
    username_field = driver.find_element(By.NAME, "uid")  # Adjust 'uid' if necessary
    username_field.send_keys(username)

    # Find and fill the password field
    password_field = driver.find_element(By.NAME, "password")  # Adjust 'password' if necessary
    password_field.send_keys(password)

    # Submit the login form
    driver.find_element(By.NAME, "btnLogin").click()  # Adjust 'btnLogin' if necessary

    # Wait for the element with class "heading3" and specific marquee text to confirm login
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Welcome To Manager's Page of Guru99 Bank"
        )
    )
    # Open the target page
    driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")


# Login at the start of your test
login("mngr595557", "sApEgad")


def reload_page():
    """Reload the page to reset form fields."""
    driver.refresh()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "cusid"))
    )


# Utility functions for error checking
def check_error_message(element_id, expected_message):
    message_element = driver.find_element(By.ID, element_id)
    assert message_element.text == expected_message, f"Expected '{expected_message}', but got '{message_element.text}'"


def test_blank_customer_id():
    """Test Case: Leave Customer ID blank and move to the next field using Tab."""
    reload_page()
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Customer ID is required")


def test_special_characters_in_customer_id():
    """Test Case: Enter special characters in Customer ID and move to the next field using Tab."""
    reload_page()
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys("@#$$%")
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Special characters are not allowed")


def test_letters_in_customer_id():
    """Test Case: Enter letters in Customer ID and move to the next field using Tab."""
    reload_page()
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.clear()
    customer_id_field.send_keys("ABC123")
    customer_id_field.send_keys(Keys.TAB)
    check_error_message("message14", "Characters are not allowed")


def test_blank_initial_deposit():
    """Test Case: Leave Initial Deposit blank and move to the next field using Tab."""
    reload_page()
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Initial Deposit must not be blank")


def test_special_characters_in_initial_deposit():
    """Test Case: Enter special characters in Initial Deposit and move to the next field using Tab."""
    reload_page()
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys("#$%123")
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Special characters are not allowed")


def test_letters_in_initial_deposit():
    """Test Case: Enter letters in Initial Deposit and move to the next field using Tab."""
    reload_page()
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.clear()
    initial_deposit_field.send_keys("DepositABC")
    initial_deposit_field.send_keys(Keys.TAB)
    check_error_message("message19", "Characters are not allowed")


def test_initial_deposit_below_minimum():
    """Test Case: Enter valid Customer ID and an Initial Deposit below the minimum."""
    driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")
    driver.find_element(By.NAME, "cusid").send_keys("47674", Keys.TAB)
    driver.find_element(By.NAME, "inideposit").send_keys("5")
    driver.find_element(By.NAME, "button2").click()

    # Check if alert is displayed
    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    assert alert.text == "Initial deposit must be 500 or more", f"Expected alert message not found. Got '{alert.text}'"
    alert.accept()
    print("Success: Minimum deposit alert displayed.")


def test_successful_submission():
    """Test Case: Enter valid Customer ID and Initial Deposit and submit."""
    reload_page()
    driver.find_element(By.NAME, "cusid").send_keys("47674", Keys.TAB)
    driver.find_element(By.NAME, "inideposit").send_keys("5000")
    driver.find_element(By.NAME, "button2").click()

    # Wait for success message and account detail table
    try:
        success_message = WebDriverWait(driver, 10).until(
            ec.text_to_be_present_in_element(
                (By.CLASS_NAME, "heading3"), "Account Generated Successfully!!!"
            )
        )
        assert success_message, "Success message not found."
        print("Success: Account creation success message displayed.")
    except Exception as e:
        print(f"Failure: {str(e)}")


def run_test(test_func):
    """Run a test and log if it passes or fails."""
    try:
        test_func()  # Run the test function
        test_results.append((test_func.__name__, "PASS"))
        print(f"Success: {test_func.__name__}")
    except AssertionError as e:
        test_results.append((test_func.__name__, "FAIL", str(e)))
        print(f"Failure: {test_func.__name__} - {str(e)}")
    except Exception as e:
        test_results.append((test_func.__name__, "ERROR", traceback.format_exc()))
        print(f"Error in {test_func.__name__}: {str(e)}")


# Run tests using run_test
for test in [
    test_blank_customer_id,
    test_special_characters_in_customer_id,
    test_letters_in_customer_id,
    test_blank_initial_deposit,
    test_special_characters_in_initial_deposit,
    test_letters_in_initial_deposit,
    test_successful_submission,
    test_initial_deposit_below_minimum
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
