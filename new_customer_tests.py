from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/addcustomerpage.php")  # Replace with actual URL


def reload_page():
    driver.refresh()  # Refresh the page
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "name"))
    )


# Test Functions
# T4: Numbers not allowed in Customer Name
def test_customer_name_no_numbers():
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys("12345")
    name_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message").text
    assert "Numbers are not allowed" in error_message, "Expected error for numbers in Customer Name not displayed"
    reload_page()


# T5: Special characters not allowed in Customer Name
def test_customer_name_no_special_characters():
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys("@#$%")
    name_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Customer "
                                                                   "Name not displayed")
    reload_page()


# T6: Customer Name must not be blank
def test_customer_name_not_blank():
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message").text
    assert "Customer name must not be blank" in error_message, "Expected error for blank Customer Name not displayed"
    reload_page()


# T7: Customer Name - First character cannot have space
def test_customer_name_no_leading_space():
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys(" John")
    name_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in Customer Name "
                                                                   "not displayed")
    reload_page()


# T8: Address must not be blank
def test_address_not_blank():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message3").text
    assert "Address Field must not be blank" in error_message, "Expected error for blank Address not displayed"
    reload_page()


# T9: Address - First character cannot have space
def test_address_no_leading_space():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.send_keys(" 123 Main St")
    address_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message3").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in Address not "
                                                                   "displayed")
    reload_page()


# T10: Address - Special characters not allowed
def test_address_no_special_characters():
    address_field = driver.find_element(By.NAME, "addr")
    address_field.send_keys("123 Main St@!")
    address_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message3").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Address "
                                                                   "not displayed")
    reload_page()


# T11: City - Special characters not allowed
def test_city_no_special_characters():
    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("City@!")
    city_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message4").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in City not "
                                                                   "displayed")
    reload_page()


# T12: City - City Field must not be blank
def test_city_not_blank():
    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message4").text
    assert "City Field must not be blank" in error_message, "Expected error for blank City not displayed"
    reload_page()


# T13: City - Numbers are not allowed
def test_city_no_numbers():
    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("City123")
    city_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message4").text
    assert "Numbers are not allowed" in error_message, "Expected error for numbers in City not displayed"
    reload_page()


# T14: City - First character cannot have space
def test_city_no_leading_space():
    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys(" City")
    city_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message4").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in City not "
                                                                   "displayed")
    reload_page()


# T15: State - Numbers are not allowed
def test_state_no_numbers():
    state_field = driver.find_element(By.NAME, "state")
    state_field.send_keys("State123")
    state_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message5").text
    assert "Numbers are not allowed" in error_message, "Expected error for numbers in State not displayed"
    reload_page()


# T16: State must not be blank
def test_state_not_blank():
    state_field = driver.find_element(By.NAME, "state")
    state_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message5").text
    assert "State must not be blank" in error_message, "Expected error for blank State not displayed"
    reload_page()


# T17: State - Special characters are not allowed
def test_state_no_special_characters():
    state_field = driver.find_element(By.NAME, "state")
    state_field.send_keys("State@!")
    state_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message5").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in State not "
                                                                   "displayed")
    reload_page()


# T17.1: State - First character cannot have space
def test_state_no_leading_space():
    state_field = driver.find_element(By.NAME, "state")
    state_field.send_keys(" State")
    state_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message5").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in State not "
                                                                   "displayed")
    reload_page()


# T18: PIN - Characters are not allowed
def test_pin_no_characters():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.send_keys("ABCDEF")
    pin_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message6").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in PIN not displayed"
    reload_page()


# T19: PIN - PIN Code must not be blank
def test_pin_not_blank():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message6").text
    assert "PIN Code must not be blank" in error_message, "Expected error for blank PIN not displayed"
    reload_page()


# T20: PIN - Special characters are not allowed
def test_pin_no_special_characters():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.send_keys("1234@!")
    pin_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message6").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in PIN not "
                                                                   "displayed")
    reload_page()


# T21: PIN - PIN Code must have 6 Digits
def test_pin_six_digits():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.send_keys("12345")  # Enter only 5 digits
    pin_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message6").text
    assert "PIN Code must have 6 Digits" in error_message, ("Expected error for PIN with less than 6 digits not "
                                                            "displayed")
    reload_page()


# T22: PIN - First character cannot have space
def test_pin_no_leading_space():
    pin_field = driver.find_element(By.NAME, "pinno")
    pin_field.send_keys(" 123456")
    pin_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message6").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in PIN not "
                                                                   "displayed")
    reload_page()


# T23: Telephone Number - Must not be blank
def test_telephone_not_blank():
    telephone_field = driver.find_element(By.NAME, "telephoneno")
    telephone_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message7").text
    assert "Mobile no must not be blank" in error_message, "Expected error for blank Telephone not displayed"
    reload_page()


# T24: Telephone Number - Special characters are not allowed
def test_telephone_no_special_characters():
    telephone_field = driver.find_element(By.NAME, "telephoneno")
    telephone_field.send_keys("1234@!")
    telephone_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message7").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Telephone "
                                                                   "not displayed")
    reload_page()


# T25: Telephone Number - Characters are not allowed
def test_telephone_no_characters():
    telephone_field = driver.find_element(By.NAME, "telephoneno")
    telephone_field.send_keys("abcd")
    telephone_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message7").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Telephone not displayed"
    reload_page()


# T26: Telephone Number - First character cannot have space
def test_telephone_no_leading_space():
    telephone_field = driver.find_element(By.NAME, "telephoneno")
    telephone_field.send_keys(" 1234567890")
    telephone_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message7").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in Telephone not "
                                                                   "displayed")
    reload_page()


# T27: Email - Must not be blank
def test_email_not_blank():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message9").text
    assert "Email-ID must not be blank" in error_message, "Expected error for blank Email not displayed"
    reload_page()


# T28: Email - Invalid format
def test_email_invalid_format():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.send_keys("invalid-email")
    email_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message9").text
    assert "Email-ID is not valid" in error_message, "Expected error for invalid Email format not displayed"
    reload_page()


# T29: Email - First character cannot have space
def test_email_no_leading_space():
    email_field = driver.find_element(By.NAME, "emailid")
    email_field.send_keys(" user@domain.com")
    email_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message9").text
    assert "First character can not have space" in error_message, ("Expected error for leading space in Email not "
                                                                   "displayed")
    reload_page()


try:
    # Run tests in order
    test_customer_name_no_numbers()  # T4
    test_customer_name_no_special_characters()  # T5
    test_customer_name_not_blank()  # T6
    test_customer_name_no_leading_space()  # T7
    test_address_not_blank()  # T8
    test_address_no_leading_space()  # T9
    test_address_no_special_characters()  # T10
    test_city_no_special_characters()  # T11
    test_city_not_blank()  # T12
    test_city_no_numbers()  # T13
    test_city_no_leading_space()  # T14
    test_state_no_numbers()  # T15
    test_state_not_blank()  # T16
    test_state_no_special_characters()  # T17
    test_state_no_leading_space()  # T17.1
    test_pin_no_characters()  # T18
    test_pin_not_blank()  # T19
    test_pin_no_special_characters()  # T20
    test_pin_six_digits()  # T21
    test_pin_no_leading_space()  # T22
    test_telephone_not_blank()  # T23
    test_telephone_no_special_characters()  # T24
    test_telephone_no_characters()  # T25
    test_telephone_no_leading_space()  # T26
    test_email_not_blank()  # T27
    test_email_invalid_format()  # T28
    test_email_no_leading_space()  # T29

except Exception as e:
    print("Test failed:", e)

finally:
    # Close the browser after tests
    driver.quit()
