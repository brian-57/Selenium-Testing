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

# Wait object for explicit waits
wait = WebDriverWait(driver, 15)

# ActionChains for handling hover-over actions on the main menu
actions = ActionChains(driver)

# Function to fill out and submit the form
def fill_form():
    try:
        # Wait for form fields to be visible
        name_field = wait.until(EC.visibility_of_element_located((By.NAME, "your-name")))
        email_field = driver.find_element(By.NAME, "your-email")
        phone_field = driver.find_element(By.NAME, "your-phone")
        company_field = driver.find_element(By.NAME, "your-company")
        message_field = driver.find_element(By.NAME, "your-message")

        # Fill the form fields using send_keys()
        name_field.send_keys("Brian Simiyu")
        email_field.send_keys("briansimiyu102@gmail.com")
        phone_field.send_keys("0758445165")
        company_field.send_keys("Brisntech Technologies")
        message_field.send_keys("How do I get in touch?")

        time.sleep(1)

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//input[@value='Submit Now']")
        submit_button.click()

        # Wait for the form to process and get the success/failure message
        try:
            success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wpcf7-response-output"))).text
            if "error trying to send your message" in success_message.lower():
                print(f"FAIL: Form submission failed. Message displayed: {success_message}")
            else:
                print(f"PASS: Form submission message: {success_message}")
        except Exception as e:
            print(f"FAIL: No success message found. Exception: {e}")

    except Exception as e:
        print(f"FAIL: Could not fill out the form. Exception: {e}")

# Navigation logic to different forms
menu_navigation = {
    "Services": [
        "Testing as a Service – TaaS", "Staff Augmentation", "Trainings"
    ],
    "Contact": []  # Direct link
}

# Iterate over each main menu and sub-menu item to fill the form
for main_menu, sub_menus in menu_navigation.items():
    try:
        # Find and click the main menu item
        nav_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, main_menu)))
        nav_link.click()
        time.sleep(5)

        if sub_menus:
            # Iterate over sub-menu items
            for sub_menu in sub_menus:
                try:
                    # Find and click the sub-menu item
                    submenu_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, sub_menu)))
                    submenu_link.click()
                    time.sleep(3)

                    # Fill out the form
                    fill_form()

                    # Navigate back to the homepage
                    driver.get("https://tezzasolutions.com")
                    time.sleep(3)

                except Exception as e:
                    print(f"ERROR: Could not navigate to '{sub_menu}' under '{main_menu}'. Exception: {e}")
        else:
            # For direct links like Contact
            fill_form()

    except Exception as e:
        print(f"ERROR: Could not navigate to '{main_menu}'. Exception: {e}")

# Close the browser after completion
driver.quit()
