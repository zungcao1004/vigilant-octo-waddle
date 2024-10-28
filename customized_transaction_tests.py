from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php")


def reload_page():
    driver.refresh()  # Refresh the page
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "accountno"))  # Wait for the account number field to be visible
    )


# Test Functions
# T33: Account No - Account Number must not be blank
def test_account_number_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()  # Clear any existing text
    account_no_field.send_keys(Keys.TAB)  # Move focus away
    error_message = driver.find_element(By.ID, "message2").text
    assert "Account Number must not be blank" in error_message, "Expected error for blank Account Number not displayed"
    reload_page()


# T34: Account No - Characters are not allowed
def test_account_number_no_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()
    account_no_field.send_keys("abcd")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Characters are not allowed" in error_message, ("Expected error for characters in Account Number not "
                                                           "displayed")
    reload_page()


# T35: Account No - Special characters are not allowed
def test_account_number_no_special_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.clear()
    account_no_field.send_keys("@#$%")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Account "
                                                                   "Number not displayed")
    reload_page()


# T36: Minimum transaction value - Special characters are not allowed
def test_min_transaction_value_no_special_characters():
    min_transaction_field = driver.find_element(By.NAME, "amountlowerlimit")
    min_transaction_field.clear()
    min_transaction_field.send_keys("@#$%")
    min_transaction_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message12").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Minimum "
                                                                   "Transaction Value not displayed")
    reload_page()


# T38: Minimum transaction value - Characters are not allowed
def test_min_transaction_value_no_characters():
    min_transaction_field = driver.find_element(By.NAME, "amountlowerlimit")
    min_transaction_field.clear()
    min_transaction_field.send_keys("abcd")
    min_transaction_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message12").text
    assert "Characters are not allowed" in error_message, ("Expected error for characters in Minimum Transaction Value "
                                                           "not displayed")
    reload_page()


# T39: Number of transaction - Special characters are not allowed
def test_number_of_transaction_no_special_characters():
    num_transaction_field = driver.find_element(By.NAME, "numtransaction")
    num_transaction_field.clear()
    num_transaction_field.send_keys("@#$%")
    num_transaction_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message13").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Number of "
                                                                   "Transactions not displayed")
    reload_page()


# T41: Number of transaction - Characters are not allowed
def test_number_of_transaction_no_characters():
    num_transaction_field = driver.find_element(By.NAME, "numtransaction")
    num_transaction_field.clear()
    num_transaction_field.send_keys("abcd")
    num_transaction_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message13").text
    assert "Characters are not allowed" in error_message, ("Expected error for characters in Number of Transactions "
                                                           "not displayed")
    reload_page()


# T42: From Date must not be blank
def test_from_date_not_blank():
    from_date_field = driver.find_element(By.NAME, "fdate")
    from_date_field.click()
    from_date_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message26").text
    assert "From Date Field must not be blank" in error_message, "Expected error for blank From Date not displayed"
    reload_page()


# T43: To Date must not be blank
def test_to_date_not_blank():
    to_date_field = driver.find_element(By.NAME, "tdate")
    to_date_field.click()
    to_date_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message27").text
    assert "To Date Field must not be blank" in error_message, "Expected error for blank To Date not displayed"
    reload_page()


try:
    # Run tests in order
    test_account_number_not_blank()
    test_account_number_no_characters()
    test_account_number_no_special_characters()
    test_min_transaction_value_no_special_characters()
    test_min_transaction_value_no_characters()
    test_number_of_transaction_no_special_characters()
    test_number_of_transaction_no_characters()
    test_from_date_not_blank()
    test_to_date_not_blank()

except Exception as e:
    print("Test failed:", e)

finally:
    # Close the browser after tests
    driver.quit()
