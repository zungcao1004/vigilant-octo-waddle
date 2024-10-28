from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

# Initialize the WebDriver
driver = webdriver.Firefox()

print("Current session is {}".format(driver.session_id))

try:
    driver.get("https://www.demo.guru99.com/V4/manager/Logout.php")

    # Wait for an alert to be present and switch to it
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)

    # You can now retrieve the text from the alert
    alert_text = alert.text
    assert "You Have Succesfully Logged Out!!" in alert_text, "Something wrong when logging out"

    # Optionally accept the alert
    alert.accept()

except Exception as e:
    print("Error occurred:")
    print(e)
finally:
    # Close the browser
    driver.quit()
