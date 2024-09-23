from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Set up the browser
driver = webdriver.Firefox()
driver.get("https://tezzasolutions.com")
driver.maximize_window()

# ActionChains for handling hover-over actions on the main menu
actions = ActionChains(driver)

# Waits
wait = WebDriverWait(driver, 10)


# Function to scroll down to the form area and fill out the form
def fill_out_consultation_form():
    # Scroll to the form area
    form_element = wait.until(EC.presence_of_element_located((By.NAME, "your-name")))
    driver.execute_script("arguments[0].scrollIntoView();", form_element)
    time.sleep(2)

    # Fill in the form
    name_field = driver.find_element(By.NAME, "your-name")
    name_field.click()
    name_field.clear()
    name_field.send_keys("Brian Simiyu")

    email_field = driver.find_element(By.NAME, "your-email")
    email_field.click()
    email_field.clear()
    email_field.send_keys("briansimiyu102@gmail.com")

    phone_field = driver.find_element(By.NAME, "your-phone")
    phone_field.click()
    phone_field.clear()
    phone_field.send_keys("0745807833")

    company_field = driver.find_element(By.NAME, "your-company")
    company_field.click()
    company_field.clear()
    company_field.send_keys("Tech Innovators Ltd")

    message_field = driver.find_element(By.NAME, "your-message")
    message_field.click()
    message_field.clear()
    message_field.send_keys("Requesting a free consultation regarding automation services.")

    time.sleep(1)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@value='Submit Now']")
    submit_button.click()

    # Wait for the form submission response
    time.sleep(5)

    # Verify the form submission success message
    try:
        success_message = driver.find_element(By.CLASS_NAME, "wpcf7-response-output").text
        if "Successfully Submitted" in success_message or "received" in success_message.lower():
            print("PASS: Form submitted successfully.")
        else:
            print(f"FAIL: Form submission failed. Message displayed: {success_message}")
    except Exception as e:
        print(f"FAIL: No success message found. Exception: {e}")


# List of sub-menu items and their corresponding main menu categories
menu_navigation = {
    "Company": ["About", "History"]
}

# Iterate over each main menu and sub-menu item to fill the form
for main_menu, sub_menus in menu_navigation.items():
    try:
        # Hover over the main menu item (Company, Services)
        nav_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, main_menu)))
        actions.move_to_element(nav_link).perform()
        time.sleep(2)

        # Iterate over sub-menu items (About, History, AI Automation Tools)
        for sub_menu in sub_menus:
            try:
                # Locate and click the sub-menu link
                submenu_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, sub_menu)))
                submenu_link.click()
                time.sleep(3)

                # Fill out the consultation form
                fill_out_consultation_form()

                # Navigate back to the homepage to test the next page
                driver.get("https://tezzasolutions.com")
                time.sleep(3)

                # Hover over the main menu again after returning
                nav_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, main_menu)))
                actions.move_to_element(nav_link).perform()
                time.sleep(2)

            except Exception as e:
                print(f"ERROR: Could not navigate to '{sub_menu}' under '{main_menu}'. Exception: {e}")

    except Exception as e:
        print(f"ERROR: Could not hover over '{main_menu}' or complete the form. Exception: {e}")

# Close the browser after completion
driver.quit()
