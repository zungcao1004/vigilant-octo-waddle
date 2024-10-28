from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/WithdrawalInput.php")


def reload_page():
    driver.refresh()  # Refresh the page
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "accountno"))  # Wait for the account number field to be visible
    )


# Test Functions
# T104: Account No must not be blank
def test_account_no_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message2").text
    assert "Account Number must not be blank" in error_message, "Expected error for blank Account No not displayed"
    reload_page()


# T105: Special characters not allowed in Account No
def test_account_no_no_special_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("@#$%")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Account No"
                                                                   "not displayed")
    reload_page()


# T106: Characters not allowed in Account No
def test_account_no_no_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("abcd")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Account No not displayed"
    reload_page()


# T107: Amount field must not be blank
def test_amount_not_blank():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message1").text
    assert "Amount field must not be blank" in error_message, "Expected error for blank Amount field not displayed"
    reload_page()


# T108: Characters not allowed in Amount field
def test_amount_no_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("abcde")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Amount field not displayed"
    reload_page()


# T109: Special characters not allowed in Amount field
def test_amount_no_special_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("!@#$")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Amount "
                                                                   "field not displayed")
    reload_page()


# T110: Description must not be blank
def test_description_not_blank():
    description_field = driver.find_element(By.NAME, "desc")
    description_field.send_keys(Keys.TAB)  # Move to the next field
    error_message = driver.find_element(By.ID, "message17").text
    assert "Description can not be blank" in error_message, "Expected error for blank Description not displayed"
    reload_page()


try:
    # Run tests
    test_account_no_not_blank()
    test_account_no_no_special_characters()
    test_account_no_no_characters()
    test_amount_not_blank()
    test_amount_no_characters()
    test_amount_no_special_characters()
    test_description_not_blank()

except Exception as e:
    print("Test failed:", e)

finally:
    # Close the browser after tests
    driver.quit()
