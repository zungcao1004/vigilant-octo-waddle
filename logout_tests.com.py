from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import traceback


# Utility function for initializing WebDriver
def init_driver():
    return webdriver.Chrome()


# Utility function for closing WebDriver
def close_driver(driver):
    driver.quit()


# List to track test results
test_results = []


# Function to run each test case
def run_test(test_func):
    driver = init_driver()  # Initialize WebDriver for each test
    try:
        test_func(driver)
        test_results.append((test_func.__name__, "PASS"))
    except AssertionError as e:
        test_results.append((test_func.__name__, "FAIL", str(e)))
    except Exception:
        test_results.append((test_func.__name__, "ERROR", traceback.format_exc()))
    finally:
        close_driver(driver)  # Ensure the driver is closed after each test


# Test Cases
def logout_with_valid_session(driver):
    driver.get("https://www.demo.guru99.com/V4/index.php")
    username_field = driver.find_element(By.NAME, "uid")
    username_field.send_keys("mngr595557")
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("sApEgad")
    driver.find_element(By.NAME, "btnLogin").click()
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CLASS_NAME, "heading3"), "Welcome To Manager's Page of Guru99 Bank"
        )
    )

    # Logout
    logout_link = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    )
    logout_link.click()
    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    assert "Successfully Logged Out" in alert.text, f"Expected 'Successfully Logged Out', but got: '{alert.text}'"
    alert.accept()  # Accept the alert to close it


def logout_with_invalid_session(driver):
    driver.get("https://www.demo.guru99.com/V4/manager/Managerhomepage.php")
    logout_link = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    )
    logout_link.click()
    alert = WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert_text = alert.text
    # Check if the alert indicates a successful logout
    if "Logged Out" in alert_text:
        raise AssertionError("Logout was unexpectedly successful, should not have logged out.")
    else:
        raise AssertionError("Unexpected alert text: " + alert_text)


# Running each test and storing results
run_test(logout_with_valid_session)
run_test(logout_with_invalid_session)

# Print test results summary
print("\nTest Results:")
for result in test_results:
    if len(result) == 2:
        print(f"{result[0]}: {result[1]}")
    else:
        print(f"{result[0]}: {result[1]} - {result[2]}")
