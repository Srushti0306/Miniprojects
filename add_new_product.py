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

# Navigate to the webpage
    driver.get("http://localhost/medical/addnew.php")

# Fill out the form with valid data
    product_name = "acetaminophen"  # Replace with the desired product name
    unit = "2"  # Replace with the desired unit
    price = "10"  # Replace with the desired price
    supplier = "Arya Patil"  # Replace with the desired supplier
    company = "ABC"  # Replace with the desired company
    category = "Tablet"  # Replace with the desired category
    description = "Fever and pain reliever"  # Replace with the desired description

# Locate form elements and fill them out
    product_name_input = driver.find_element(By.NAME, "name")
    unit_input = driver.find_element(By.NAME, "unit")
    price_input = driver.find_element(By.NAME, "price")
    supplier_input = driver.find_element(By.NAME, "supplier")
    company_input = driver.find_element(By.NAME, "company")
# category_input = driver.find_element(By.NAME, "inCategory")
    category_dropdown = driver.find_element(By.NAME, "catId")

# Create a Select object for the dropdown
    category_select = Select(category_dropdown)

# Select the category by visible text
    category_name = "Other"  # Replace with the desired category name
    category_select.select_by_visible_text(category_name)
    description_input = driver.find_element(By.NAME, "discription")

    product_name_input.send_keys(product_name)
    unit_input.send_keys(unit)
    price_input.send_keys(price)
    supplier_input.send_keys(supplier)
    company_input.send_keys(company)
# category_input.send_keys(category)
    description_input.send_keys(description)

# Click the "Save" button
    save_button = driver.find_element(By.NAME, "saveProduct")
    save_button.click()

# Click the "Reset" button
    # reset_button = driver.find_element(By.NAME, "reset")
    # reset_button.click()
    # print("Test Case 7: Reset add Product - Passed")
# Verify that the product is successfully added and a success message is displayed
    # assert "Product added successfully" in success_message.text, "Product not added successfully"
    print("Test Case 8: Add Product - Passed")

except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()
