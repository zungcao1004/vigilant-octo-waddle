from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.demo.guru99.com/V4/manager/addcustomerpage.php")


def check_error_message(element_id, expected_message):
    """Check if the error message for a field is as expected."""
    message_element = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.ID, element_id))
    )
    assert expected_message in message_element.text, f"Expected: '{expected_message}', but got: '{message_element.text}'"


def reload_page():
    """Reload the page to reset form fields."""
    driver.refresh()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "name"))
    )


# Define functions for each test case

# Customer Name Field Validation
def test_blank_customer_name():
    reload_page()
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
    check_error_message("message", "Customer name must not be blank")


def test_customer_name_with_numbers():
    reload_page()
    driver.find_element(By.NAME, "name").send_keys("12345")
    driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
    check_error_message("message", "Numbers are not allowed")


def test_customer_name_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "name").send_keys("!@#$$%")
    driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
    check_error_message("message", "Special characters are not allowed")


def test_customer_name_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "name").send_keys(" John Doe")
    driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
    check_error_message("message", "First character can not have space")


# Date of Birth Validation
def test_blank_date_of_birth():
    reload_page()
    dob = driver.find_element(By.NAME, "dob")
    dob.clear()
    dob.send_keys(Keys.TAB)
    check_error_message("message24", "Date Field must not be blank")


# Address Field Validation
def test_blank_address():
    reload_page()
    driver.find_element(By.NAME, "addr").clear()
    driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
    check_error_message("message3", "Address Field must not be blank")


def test_address_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "addr").send_keys("*&^%$#@")
    driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
    check_error_message("message3", "Special characters are not allowed")


def test_address_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "addr").send_keys(" 123 Main St.")
    driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
    check_error_message("message3", "First character can not have space")


# City Field Validation
def test_blank_city():
    reload_page()
    driver.find_element(By.NAME, "city").clear()
    driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
    check_error_message("message4", "City Field must not be blank")


def test_city_with_numbers():
    reload_page()
    driver.find_element(By.NAME, "city").send_keys("12345")
    driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
    check_error_message("message4", "Numbers are not allowed")


def test_city_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "city").send_keys("!@# New York")
    driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
    check_error_message("message4", "Special characters are not allowed")


def test_city_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "city").send_keys(" New York")
    driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
    check_error_message("message4", "First character can not have space")


# State Field Validation
def test_blank_state():
    reload_page()
    driver.find_element(By.NAME, "state").clear()
    driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
    check_error_message("message5", "State must not be blank")


def test_state_with_numbers():
    reload_page()
    driver.find_element(By.NAME, "state").send_keys("12345")
    driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
    check_error_message("message5", "Numbers are not allowed")


def test_state_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "state").send_keys("California!")
    driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
    check_error_message("message5", "Special characters are not allowed")


def test_state_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "state").send_keys(" California")
    driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
    check_error_message("message5", "First character can not have space")


# PIN Field Validation
def test_pin_with_less_than_six_digits():
    reload_page()
    driver.find_element(By.NAME, "pinno").send_keys("123")
    driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
    check_error_message("message6", "PIN Code must have 6 Digits")


def test_pin_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "pinno").send_keys("12345!")
    driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
    check_error_message("message6", "Special characters are not allowed")


def test_pin_with_characters():
    reload_page()
    driver.find_element(By.NAME, "pinno").send_keys("abcd")
    driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
    check_error_message("message6", "Characters are not allowed")


def test_pin_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "pinno").send_keys(" 123456")
    driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
    check_error_message("message6", "First character can not have space")


# Mobile Number Field Validation
def test_blank_mobile_number():
    reload_page()
    driver.find_element(By.NAME, "telephoneno").clear()
    driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
    check_error_message("message7", "Mobile no must not be blank")


def test_mobile_number_with_characters():
    reload_page()
    driver.find_element(By.NAME, "telephoneno").send_keys("abcd1234")
    driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
    check_error_message("message7", "Characters are not allowed")


def test_mobile_number_with_special_characters():
    reload_page()
    driver.find_element(By.NAME, "telephoneno").send_keys("123-456!")
    driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
    check_error_message("message7", "Special characters are not allowed")


def test_mobile_number_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "telephoneno").send_keys(" 1234567890")
    driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
    check_error_message("message7", "First character can not have space")


# Email Field Validation
def test_blank_email():
    reload_page()
    driver.find_element(By.NAME, "emailid").clear()
    driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
    check_error_message("message9", "Email-ID must not be blank")


def test_email_with_invalid_format():
    reload_page()
    driver.find_element(By.NAME, "emailid").send_keys("invalid-email-format")
    driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
    check_error_message("message9", "Email-ID is not valid")


def test_email_with_leading_space():
    reload_page()
    driver.find_element(By.NAME, "emailid").send_keys(" john.doe@example.com")
    driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
    check_error_message("message9", "First character can not have space")


def test_successful_form_submission():
    reload_page()

    # Fill in all fields with valid data
    driver.find_element(By.NAME, "name").send_keys("John Doe")
    driver.find_element(By.NAME, "dob").send_keys("01/01/1990")
    driver.find_element(By.NAME, "addr").send_keys("123 Main St")
    driver.find_element(By.NAME, "city").send_keys("New York")
    driver.find_element(By.NAME, "state").send_keys("NY")
    driver.find_element(By.NAME, "pinno").send_keys("123456")
    driver.find_element(By.NAME, "telephoneno").send_keys("1234567890")
    driver.find_element(By.NAME, "emailid").send_keys("john.doe@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")

    # Submit the form
    driver.find_element(By.NAME, "sub").click()


# Run all test cases
try:
    test_blank_customer_name()
    test_customer_name_with_numbers()
    test_customer_name_with_special_characters()
    test_customer_name_with_leading_space()
    test_blank_date_of_birth()
    test_blank_address()
    test_address_with_special_characters()
    test_address_with_leading_space()
    test_blank_city()
    test_city_with_numbers()
    test_city_with_special_characters()
    test_city_with_leading_space()
    test_blank_state()
    test_state_with_numbers()
    test_state_with_special_characters()
    test_state_with_leading_space()
    test_pin_with_less_than_six_digits()
    test_pin_with_special_characters()
    test_pin_with_characters()
    test_pin_with_leading_space()
    test_blank_mobile_number()
    test_mobile_number_with_characters()
    test_mobile_number_with_special_characters()
    test_mobile_number_with_leading_space()
    test_blank_email()
    test_email_with_invalid_format()
    test_email_with_leading_space()
    test_successful_form_submission()
    print("All tests completed.")
except Exception as e:
    print("Error occurred:", e)
finally:
    driver.quit()
