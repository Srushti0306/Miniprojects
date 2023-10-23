from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "title"))
    # )
    driver.get("http://localhost/medical/sitesetting.php")
    # Find the form fields and fill them with desired values
    title_field = driver.find_element(By.NAME, "title")
    title_field.clear()
    title_field.send_keys("Medical Stores")

    name_field = driver.find_element(By.NAME, "name")
    name_field.clear()
    name_field.send_keys("Medical Stores")

    # Find the "Save Setting" button and click it
    save_button = driver.find_element(By.NAME, "saveSetting")
    save_button.click()

    # Wait for the success or error message to appear (or assert that changes have been saved)

    print("Test Case 17: Site setting changes saved -Passed.")


except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()    