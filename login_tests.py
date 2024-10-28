from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()

print("Current session is {}".format(driver.session_id))

try:
    # Open the login page
    driver.get("https://www.demo.guru99.com/V4/index.php")

    # Test Case T92: User-ID must not be blank
    def test_user_id_not_blank():
        # Step 1: Type something in uid field, then delete it
        user_id_field = driver.find_element(By.NAME, "uid")
        user_id_field.send_keys("test_user_id")
        user_id_field.clear()  # Clear to leave it blank

        # Step 2: Press "Tab" to move to password field
        user_id_field.send_keys(Keys.TAB)

        # Check that the error message for User-ID becomes visible
        error_message_visible = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.ID, "message23"))
        )
        assert error_message_visible, "Expected error message not displayed for blank User-ID"

    # Test Case T93: Password must not be blank
    def test_password_not_blank():
        # Step 1: Enter a valid User-ID
        user_id_field = driver.find_element(By.NAME, "uid")
        user_id_field.send_keys("valid_user_id")

        # Step 2: Press "Tab" to move to password field
        user_id_field.send_keys(Keys.TAB)

        # Step 3: Type something in password field, then delete it
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("test_password")
        password_field.clear()  # Clear to leave it blank

        # Step 4: Press "Tab" to move to the btnLogin
        password_field.send_keys(Keys.TAB)

        # Check that the error message for Password becomes visible
        error_message_visible = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.ID, "message18"))
        )
        assert error_message_visible, "Expected error message not displayed for blank Password"

    def reload_page():
        """Function to reload the page and wait for the User-ID field to be available."""
        driver.refresh()  # Refresh the page
        WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.NAME, "uid"))  # Wait for the uid field to be visible
        )

    # Run test cases
    test_user_id_not_blank()
    reload_page()
    test_password_not_blank()

except Exception as e:
    print("Error occurred:")
    print(e)
finally:
    # Close the browser
    driver.quit()
