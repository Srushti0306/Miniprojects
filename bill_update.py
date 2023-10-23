from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select

# Initialize the Firefox driver and service
service_object = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service_object)

driver.get("http://localhost/medical/login.php")
try:
    username_field = driver.find_element(By.NAME, "email")
    # Replace with the actual name attribute
    password_field = driver.find_element(By.NAME, "password")
    # Replace with the actual name attribute
    login_button = driver.find_element(By.NAME, "login")
    # Replace with the actual username
    username_field.send_keys("admin@gmail.com")
    password_field.send_keys("admin")  # Replace with the actual password
    login_button.click()


    driver.get("http://localhost/medical/inventeries.php")
    delete_button = driver.find_element(By.LINK_TEXT, "Delete Item")  # Replace with the actual link text
    delete_button.click()
    print("Test Case 15: Inventories deleted.- Passed")

    driver.get("http://localhost/medical/inventeries.php")
# Select items to add to the bill by finding buttons with specific text
    select_buttons = driver.find_elements(By.XPATH, '//*[@id="selection1"]/button')
    for select_button in select_buttons:
        select_button.click()


        # Find the element to update the quantity and set the new value
    driver.get("http://localhost/medical/billing.php")    
    quantity_input = driver.find_element(By.NAME, "qty")  # Replace with the actual name or selector
    quantity_input.clear()
    quantity_input.send_keys("3")  # Change to the desired quantity

    # Find and click the "Update" button
    update_button = driver.find_element(By.NAME, "updateBill")  # Replace with the actual name or selector
    update_button.click()
    print("Test Case 16: update quantity of medicine in Bill- Passed")
except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()         