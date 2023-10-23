from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Test Case 3: Delete Category
    # driver.get("http://localhost/medical/manageCat.php")  # Navigate to the categories management page

# Navigate to the categories page
    driver.get("http://localhost/medical/index.php")
    manage_categories_button  = driver.find_element(By.NAME,"manage_cat")
    manage_categories_button.click()
    driver.get("http://localhost/medical/manageCat.php")
# Find and click the "Delete" button for the category you want to delete
    category_name_to_delete = "Other"  # Replace with the actual category name
    delete_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete")
    delete_button.click()
    print("Test Case 6: Delete category - Passed")


except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the WebDriver when testing is done
driver.quit()      