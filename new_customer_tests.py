from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import traceback
import random
import string


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
    driver.get("https://www.demo.guru99.com/V4/manager/addcustomerpage.php")  # Navigate to Add Customer page


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
def test_customer_name_blank():
    customer_name_field = driver.find_element(By.NAME, "name")
    customer_name_field.clear()
    customer_name_field.send_keys(Keys.TAB)
    check_error_message("message", "Customer name must not be blank")


def test_customer_name_numbers():
    customer_name_field = driver.find_element(By.NAME, "name")
    customer_name_field.clear()
    customer_name_field.send_keys("12345")
    customer_name_field.send_keys(Keys.TAB)
    check_error_message("message", "Numbers are not allowed")


def test_customer_name_special_characters():
    customer_name_field = driver.find_element(By.NAME, "name")
    customer_name_field.clear()
    customer_name_field.send_keys("!@#$$%")
    customer_name_field.send_keys(Keys.TAB)
    check_error_message("message", "Special characters are not allowed")


def test_customer_name_leading_space():
    customer_name_field = driver.find_element(By.NAME, "name")
    customer_name_field.clear()
    customer_name_field.send_keys(" John Doe")
    customer_name_field.send_keys(Keys.TAB)
    check_error_message("message", "First character can not have space")


def test_date_of_birth_blank():
    dob_field = driver.find_element(By.NAME, "dob")
    dob_field.clear()
    dob_field.send_keys(Keys.TAB)
    check_error_message("message24", "Date Field must not be blank")


def test_address_blank():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.clear()
    address_field.send_keys(Keys.TAB)
    check_error_message("message3", "Address Field must not be blank")


def test_address_special_characters():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.clear()
    address_field.send_keys("*&^%$#@")
    address_field.send_keys(Keys.TAB)
    check_error_message("message3", "Special characters are not allowed")


def test_address_leading_space():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.clear()
    address_field.send_keys(" 123 Main St.")
    address_field.send_keys(Keys.TAB)
    check_error_message("message3", "First character can not have space")


def test_city_blank():
    city_field = driver.find_element(By.NAME, "city")
    city_field.clear()
    city_field.send_keys(Keys.TAB)
    check_error_message("message4", "City Field must not be blank")


def test_city_numbers():
    city_field = driver.find_element(By.NAME, "city")
    city_field.clear()
    city_field.send_keys("12345")
    city_field.send_keys(Keys.TAB)
    check_error_message("message4", "Numbers are not allowed")


def test_city_special_characters():
    city_field = driver.find_element(By.NAME, "city")
    city_field.clear()
    city_field.send_keys("!@# New York")
    city_field.send_keys(Keys.TAB)
    check_error_message("message4", "Special characters are not allowed")


def test_city_leading_space():
    city_field = driver.find_element(By.NAME, "city")
    city_field.clear()
    city_field.send_keys(" New York")
    city_field.send_keys(Keys.TAB)
    check_error_message("message4", "First character can not have space")


def test_state_blank():
    state_field = driver.find_element(By.NAME, "state")
    state_field.clear()
    state_field.send_keys(Keys.TAB)
    check_error_message("message5", "State must not be blank")


def test_state_numbers():
    state_field = driver.find_element(By.NAME, "state")
    state_field.clear()
    state_field.send_keys("12345")
    state_field.send_keys(Keys.TAB)
    check_error_message("message5", "Numbers are not allowed")


def test_state_special_characters():
    state_field = driver.find_element(By.NAME, "state")
    state_field.clear()
    state_field.send_keys("California!")
    state_field.send_keys(Keys.TAB)
    check_error_message("message5", "Special characters are not allowed")


def test_state_leading_space():
    state_field = driver.find_element(By.NAME, "state")
    state_field.clear()
    state_field.send_keys(" California")
    state_field.send_keys(Keys.TAB)
    check_error_message("message5", "First character can not have space")


def test_pin_length():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.clear()
    pin_field.send_keys("123")
    pin_field.send_keys(Keys.TAB)
    check_error_message("message6", "PIN Code must have 6 Digits")


def test_pin_special_characters():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.clear()
    pin_field.send_keys("12345!")
    pin_field.send_keys(Keys.TAB)
    check_error_message("message6", "Special characters are not allowed")


def test_pin_characters():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.clear()
    pin_field.send_keys("abcd")
    pin_field.send_keys(Keys.TAB)
    check_error_message("message6", "Characters are not allowed")


def test_pin_leading_space():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.clear()
    pin_field.send_keys(" 123456")
    pin_field.send_keys(Keys.TAB)
    check_error_message("message6", "First character can not have space")


def test_mobile_number_blank():
    mobile_field = driver.find_element(By.NAME, "telephoneno")
    mobile_field.clear()
    mobile_field.send_keys(Keys.TAB)
    check_error_message("message7", "Mobile no must not be blank")


def test_mobile_number_characters():
    mobile_field = driver.find_element(By.NAME, "telephoneno")
    mobile_field.clear()
    mobile_field.send_keys("abcd1234")
    mobile_field.send_keys(Keys.TAB)
    check_error_message("message7", "Characters are not allowed")


def test_mobile_number_special_characters():
    mobile_field = driver.find_element(By.NAME, "telephoneno")
    mobile_field.clear()
    mobile_field.send_keys("123-456!")
    mobile_field.send_keys(Keys.TAB)
    check_error_message("message7", "Special characters are not allowed")


def test_mobile_number_leading_space():
    mobile_field = driver.find_element(By.NAME, "telephoneno")
    mobile_field.clear()
    mobile_field.send_keys(" 1234567890")
    mobile_field.send_keys(Keys.TAB)
    check_error_message("message7", "First character can not have space")


def test_email_blank():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.clear()
    email_field.send_keys(Keys.TAB)
    check_error_message("message9", "Email-ID must not be blank")


def test_email_invalid_format():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.clear()
    email_field.send_keys("invalid-email-format")
    email_field.send_keys(Keys.TAB)
    check_error_message("message9", "Email-ID is not valid")


def test_email_leading_space():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.clear()
    email_field.send_keys(" john.doe@example.com")
    email_field.send_keys(Keys.TAB)
    check_error_message("message9", "First character can not have space")


def generate_random_email():
    """Generates a random email address."""

    # Define possible characters for the username
    letters = string.ascii_lowercase
    digits = string.digits

    # Generate a random username length between 8 and 12 characters
    username_length = random.randint(8, 12)

    # Generate a random username
    username = ''.join(random.choice(letters + digits) for _ in range(username_length))

    # Choose a random domain from a list of common domains
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    domain = random.choice(domains)

    # Combine username and domain to form the email address
    email = username + "@" + domain

    return email


def test_successful_submission():
    customer_name_field = driver.find_element(By.NAME, "name")
    dob_field = driver.find_element(By.NAME, "dob")
    address_field = driver.find_element(By.NAME, "addr")
    city_field = driver.find_element(By.NAME, "city")
    state_field = driver.find_element(By.NAME, "state")
    pin_field = driver.find_element(By.NAME, "pinno")
    mobile_field = driver.find_element(By.NAME, "telephoneno")
    email_field = driver.find_element(By.NAME, "emailid")
    password_field = driver.find_element(By.NAME, "password")

    customer_name_field.clear()
    customer_name_field.send_keys("John Doe")
    dob_field.clear()
    dob_field.send_keys("01/01/1990")
    address_field.clear()
    address_field.send_keys("123 Main St")
    city_field.clear()
    city_field.send_keys("New York")
    state_field.clear()
    state_field.send_keys("NY")
    pin_field.clear()
    pin_field.send_keys("123456")
    mobile_field.clear()
    mobile_field.send_keys("1234567890")
    email_field.clear()
    email_field.send_keys(generate_random_email())
    password_field.clear()
    password_field.send_keys("123")

    driver.find_element(By.NAME, "sub").click()

    # Wait for confirmation message
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Customer Registered Successfully!!!"
        )
    )


# Execute test cases
test_cases = [
    test_customer_name_blank,
    test_customer_name_numbers,
    test_customer_name_special_characters,
    test_customer_name_leading_space,
    test_date_of_birth_blank,
    test_address_blank,
    test_address_special_characters,
    test_address_leading_space,
    test_city_blank,
    test_city_numbers,
    test_city_special_characters,
    test_city_leading_space,
    test_state_blank,
    test_state_numbers,
    test_state_special_characters,
    test_state_leading_space,
    test_pin_length,
    test_pin_special_characters,
    test_pin_characters,
    test_pin_leading_space,
    test_mobile_number_blank,
    test_mobile_number_characters,
    test_mobile_number_special_characters,
    test_mobile_number_leading_space,
    test_email_blank,
    test_email_invalid_format,
    test_email_leading_space,
    test_successful_submission,
]

for test in test_cases:
    run_test(test)

# Print test results
for result in test_results:
    print(result)

# Close the driver
driver.quit()
