from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://www.demo.guru99.com/V4/manager/addAccount.php")


def reload_page():
    driver.refresh()
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.NAME, "cusid"))
    )


# Test Functions

# T1: Customer ID is required
def test_customer_id_required():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message14").text
    assert "Customer ID is required" in error_message, "Expected error for blank Customer ID not displayed"
    reload_page()


# T2: Customer ID - Special characters are not allowed
def test_customer_id_no_special_characters():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.send_keys("@#$%")
    customer_id_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message14").text
    assert "Special characters are not allowed" in error_message, ("Expected error for special characters in Customer "
                                                                   "ID not displayed")
    reload_page()


# T3: Customer ID - Characters are not allowed
def test_customer_id_no_characters():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.send_keys("ABCD")
    customer_id_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message14").text
    assert "Characters are not allowed" in error_message, "Expected error for characters in Customer ID not displayed"
    reload_page()


# T3.1: Customer ID - First character cannot have space
def test_customer_id_no_leading_space():
    customer_id_field = driver.find_element(By.NAME, "cusid")
    customer_id_field.send_keys(" 12345")
    customer_id_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message14").text
    assert "First character can not have space" in error_message, (
        "Expected error for leading space in Customer ID not "
        "displayed")
    reload_page()


# T19: Initial Deposit - Required
def test_initial_deposit_required():
    initial_deposit_field = driver.find_element(By.NAME, "inideposit")
    initial_deposit_field.send_keys(Keys.TAB)
    error_message = driver.find_element(By.ID, "message19").text
    assert "Initial Deposit must not be blank" in error_message, ("Expected error for blank Initial Deposit not "
                                                                  "displayed")
    reload_page()


# Run Tests
try:
    test_customer_id_required()  # T1
    test_customer_id_no_special_characters()  # T2
    test_customer_id_no_characters()  # T3
    test_customer_id_no_leading_space()  # T3.1
    test_initial_deposit_required()  # T19

except Exception as e:
    print("Test failed:", e)

finally:
    driver.quit()
