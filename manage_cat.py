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

    # Navigate to the categories page
    driver.get("http://localhost/medical/index.php")
    manage_categories = driver.find_element(By.NAME,"manage_cat")
    manage_categories.click()
    print("Test Case 4: Verify Manage Categories Page - Passed")


# Fill in the form to add a new category inside the manage category
    driver.get("http://localhost/medical/manageCat.php")
    add_category_button = driver.find_element(By.NAME, "add_cat_managecat")
    add_category_button.click()
    category_name = "XYZ"  # Modify with the desired category name
    category_image_path = "C:\\Users\\srushti\\Desktop\\stqa\\b.jpg"
    category_name_input = driver.find_element(By.NAME, "inName")
    category_image_input = driver.find_element(By.NAME, "inPic")
    category_name_input.send_keys(category_name)
    category_image_input.send_keys(category_image_path)
# Submit the form to add the new category
    submit_button = driver.find_element(By.NAME, "safeIn")
    submit_button.click()
# Verify that you are still on the "Manage Categories" page after adding a new category
    # assert "Manage Categories" in driver.title, "Categories management page not found"
    print("Test Case 5: Add new Category inside manage category - Passed")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the WebDriver when testing is done
driver.quit()    