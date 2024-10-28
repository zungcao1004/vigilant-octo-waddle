from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/FundTransInput.php")


def reload_page():
    driver.refresh()  # Refresh the page
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "payersaccount"))  # Wait for the payers account field to be visible
    )


# Test Functions
# T82: Payers Account Number must not be blank
def test_payers_account_no_not_blank():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message10").text
    assert "Payers Account Number must not be blank" in error_message, ("Expected error for blank Payers Account "
                                                                        "Number not displayed")
    reload_page()


# T83: Special characters not allowed in Payers Account Number
def test_payers_account_no_no_special_characters():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("@#$%")
    payers_account_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message10").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Payers "
                                                                   "Account Number not displayed")
    reload_page()


# T84: Characters not allowed in Payers Account Number
def test_payers_account_no_no_characters():
    payers_account_field = driver.find_element(By.NAME, "payersaccount")
    payers_account_field.send_keys("abcd")
    payers_account_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message10").text
    assert "Characters are not allowed" in error_message, ("Expected error for characters in Payers Account Number not "
                                                           "displayed")
    reload_page()


# T85: Payees Account Number must not be blank
def test_payees_account_no_not_blank():
    payee_account_field = driver.find_element(By.NAME, "payeeaccount")
    payee_account_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message11").text
    assert "Payees Account Number must not be blank" in error_message, ("Expected error for blank Payees Account "
                                                                        "Number not displayed")
    reload_page()


# T86: Special characters not allowed in Payees Account Number
def test_payees_account_no_no_special_characters():
    payee_account_field = driver.find_element(By.NAME, "payeeaccount")
    payee_account_field.send_keys("@#$%")
    payee_account_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message11").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Payees "
                                                                   "Account Number not displayed")
    reload_page()


# T87: Characters not allowed in Payees Account Number
def test_payees_account_no_no_characters():
    payee_account_field = driver.find_element(By.NAME, "payeeaccount")
    payee_account_field.send_keys("abcd")
    payee_account_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message11").text
    assert "Characters are not allowed" in error_message, ("Expected error for characters in Payees Account Number not "
                                                           "displayed")
    reload_page()


# T88: Amount Field must not be blank
def test_amount_not_blank():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message1").text
    assert "Amount field must not be blank" in error_message, "Expected error for blank Amount field not displayed"
    reload_page()


# T89: Characters not allowed in Amount Field
def test_amount_no_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("abcde")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Amount field not displayed"
    reload_page()


# T90: Special characters not allowed in Amount Field
def test_amount_no_special_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("!@#$")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Amount "
                                                                   "field not displayed")
    reload_page()


# T91: Description cannot be blank
def test_description_not_blank():
    description_field = driver.find_element(By.NAME, "desc")
    description_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message17").text
    assert "Description can not be blank" in error_message, "Expected error for blank Description not displayed"
    reload_page()


try:
    # Run tests
    test_payers_account_no_not_blank()
    test_payers_account_no_no_special_characters()
    test_payers_account_no_no_characters()
    test_payees_account_no_not_blank()
    test_payees_account_no_no_special_characters()
    test_payees_account_no_no_characters()
    test_amount_not_blank()
    test_amount_no_characters()
    test_amount_no_special_characters()
    test_description_not_blank()

except Exception as e:
    print("Test failed:", e)

finally:
    # Close the browser after tests
    driver.quit()
