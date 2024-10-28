from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/DepositInput.php")  # Replace with actual URL


def reload_page():
    driver.refresh()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "accountno"))
    )


# Test Functions

# T48: Account No must not be blank
def test_account_no_not_blank():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Account Number must not be blank" in error_message, "Expected error for blank Account No not displayed"
    reload_page()


# T49: Account No - Special characters are not allowed
def test_account_no_no_special_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("@#$%")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Account "
                                                                   "No not displayed")
    reload_page()


# T50: Account No - Characters are not allowed
def test_account_no_no_characters():
    account_no_field = driver.find_element(By.NAME, "accountno")
    account_no_field.send_keys("ABC")
    account_no_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message2").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Account No not displayed"
    reload_page()


# T51: Amount field must not be blank
def test_amount_not_blank():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Amount field must not be blank" in error_message, "Expected error for blank Amount not displayed"
    reload_page()


# T52: Amount - Special characters are not allowed
def test_amount_no_special_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("@#$%")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Amount "
                                                                   "not displayed")
    reload_page()


# T53: Amount - Characters are not allowed
def test_amount_no_characters():
    amount_field = driver.find_element(By.NAME, "ammount")
    amount_field.send_keys("ABC")
    amount_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message1").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Amount not displayed"
    reload_page()


# T54: Description must not be blank
def test_description_not_blank():
    description_field = driver.find_element(By.NAME, "desc")
    description_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message17").text
    assert "Description can not be blank" in error_message, "Expected error for blank Description not displayed"
    reload_page()


# Run Tests
try:
    test_account_no_not_blank()  # T48
    test_account_no_no_special_characters()  # T49
    test_account_no_no_characters()  # T50
    test_amount_not_blank()  # T51
    test_amount_no_special_characters()  # T52
    test_amount_no_characters()  # T53
    test_description_not_blank()  # T54

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
