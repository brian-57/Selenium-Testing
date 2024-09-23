from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# Browser Set up
driver = webdriver.Firefox()
driver.get("https://tezzasolutions.com")
driver.maximize_window()
time.sleep(3)
actions = ActionChains(driver)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Find the input fields
try:
    name_field = driver.find_element(By.NAME, "your-name")
    name_field.send_keys("Brian Simiyu")

    email_field = driver.find_element(By.NAME, "your-email")
    email_field.send_keys("briansimiyu102@gmail.com")

    phone_field = driver.find_element(By.NAME, "your-phone")
    phone_field.send_keys("0745807833")

    message_field = driver.find_element(By.NAME, "your-message")
    message_field.send_keys("A functional test")

    # Submit the form without using TAB key
    submit_button = driver.find_element(By.XPATH, "//input[@value='Submit Now']")
    submit_button.click()
    time.sleep(5)  # Adjust wait time based on submission processing

    # Check Submission (Optional, can be moved before driver.quit())
    success_message = driver.find_element(By.CLASS_NAME, "wpcf7-response-output").text
    if "Successfully Submitted" in success_message or "Received" in success_message.lower():
        print("PASS:Form submitted successfully")
    else:
        error_message = driver.find_element(By.CLASS_NAME, "wpcf7-response-output").text
        print(f"FAIL:Form submission failed.Message displayed:{error_message}")

except Exception as e:
    print(f"Error:Could not complete the form submission.Exception: {e}")

finally:
    driver.quit()