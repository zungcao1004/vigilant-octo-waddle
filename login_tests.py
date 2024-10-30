from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Chrome()

print("Current session is {}".format(driver.session_id))


def check_error_message(element_id, expected_message):
    """Check if the error message for a field is as expected."""
    message_element = driver.find_element(By.ID, element_id)
    assert message_element.is_displayed(), f"Error message for {element_id} is not displayed"
    assert expected_message in message_element.text, f"Expected: '{expected_message}', but got: '{message_element.text}'"


def handle_alert(expected_text):
    """Handles the alert by checking its text and accepting it."""
    try:
        WebDriverWait(driver, 10).until(ec.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert expected_text in alert_text, f"Expected alert text: '{expected_text}', but got: '{alert_text}'"
        alert.accept()  # Close the alert
    except Exception as e:
        print(f"Alert handling failed: {e}")


def reload_page():
    """Function to reload the page and wait for the User-ID field to be available."""
    driver.refresh()  # Refresh the page
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "uid"))  # Wait for the uid field to be visible
    )


def test_blank_username_valid_password():
    """Test Case 1: Leave Username blank, enter Password."""
    user_id_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "password")

    user_id_field.click()
    password_field.send_keys("pass123")
    password_field.send_keys(Keys.TAB)  # Move to the next field
    check_error_message("message23", "User-ID must not be blank")  # Verify error message
    reload_page()


def test_valid_username_blank_password():
    """Test Case 2: Enter valid Username, leave Password blank."""
    user_id_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "password")

    user_id_field.send_keys("user123")
    password_field.click()  # Leave password blank
    password_field.send_keys(Keys.TAB)  # Move to the next field
    check_error_message("message18", "Password must not be blank")  # Verify error message
    reload_page()


def test_blank_fields_move_next():
    """Test Case 3: Leave both fields blank and move to the next element."""
    user_id_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "password")

    user_id_field.click()
    user_id_field.send_keys(Keys.TAB)  # Move to the next field
    check_error_message("message23", "User-ID must not be blank")  # Verify username error
    password_field.click()
    password_field.send_keys(Keys.TAB)  # Move to the next field
    check_error_message("message18", "Password must not be blank")  # Verify password error
    reload_page()


def test_blank_fields_submit():
    """Test Case 4: Leave both fields blank and click Submit."""
    # user_id_field = driver.find_element(By.NAME, "uid")
    # password_field = driver.find_element(By.NAME, "password")

    # Leave both fields blank and click Submit
    # user_id_field.clear()
    # password_field.clear()
    driver.find_element(By.NAME, "btnLogin").click()

    # Handle the alert after clicking submit
    handle_alert("User or Password is not valid")
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.NAME, "uid")))


def test_valid_login():
    """Test Case 5: Successfully login with valid credentials."""
    user_id_field = driver.find_element(By.NAME, "uid")
    password_field = driver.find_element(By.NAME, "password")

    user_id_field.send_keys("mngr595557")
    password_field.send_keys("sApEgad")
    driver.find_element(By.NAME, "btnLogin").click()

    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.TAG_NAME, "marquee")))

    # Verify successful login (check for the presence of an element on the landing page)
    assert "Welcome" in driver.page_source, "Login was not successful"


try:
    # Open the login page
    driver.get("https://www.demo.guru99.com/V4/index.php")

    # Run test cases
    test_blank_username_valid_password()
    test_valid_username_blank_password()
    test_blank_fields_move_next()
    test_blank_fields_submit()
    test_valid_login()

except Exception as e:
    print("Error occurred:")
    print(e)
finally:
    # Close the browser
    driver.quit()
