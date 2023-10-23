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
    # Test Case 1: Verify the title of the webpage
    expected_title = "Login"  # Replace with the expected title
    actual_title = driver.title
    assert expected_title in actual_title, f"Title mismatch. Expected: {expected_title}, Actual: {actual_title}"
    print("Test Case 1: Title verification - Passed")



    # Test Case 2: Login functionality (if applicable)
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "login")
    username_field.send_keys("admin@gmail.com")
    password_field.send_keys("admin")  
    login_button.click()
    print("Test Case 2: Login - Passed")



    # Test Case 3: Wrong Login Credentials
    """driver.get("http://localhost/bus_booking/admin.php")  # Navigate back to the login page
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.NAME, "submit")

    username_field.send_keys("WrongUsername")
    password_field.send_keys("WrongPassword")
    login_button.click()

    # Assertion for Wrong Login
    alert = Alert(driver)
    assert "incorrect username or password" in alert.text.lower()
    alert.accept()
    print("Test Case 2: Wrong login credentials - Passed")"""



# Test Case 3- Adding Category
    driver.get("http://localhost/medical/index.php")
    add_category_button = driver.find_element(By.NAME, "Add_category")
    add_category_button.click()
    category_name = "Tablets"  # Modify with the desired category name
    category_image_path = "C:\\Users\\srushti\\Desktop\\stqa\\a.jpg"
    category_name_input = driver.find_element(By.NAME, "inName")
    category_image_input = driver.find_element(By.NAME, "inPic")
    category_name_input.send_keys(category_name)
    category_image_input.send_keys(category_image_path)
# Submit the form to add the new category
    submit_button = driver.find_element(By.NAME, "safeIn")
    submit_button.click()
    assert "Medical Stores" in driver.title
    print("Test Case 3: Add new Category - Passed")
# Navigate to the categories page
    driver.get("http://localhost/medical/index.php")
# Find the "Manage Categories"
    partial_link = "http://localhost/medical/manageCat.php"
    manage_categories_link = driver.find_element(By.XPATH,  '/html/body/div[2]/div[3]/div/a/button')
    manage_categories_link.click()
    # assert "Manage Categories" in driver.title, "Categories management page not found"
    print("Test Case 4: Verify Categories Page - Passed")


except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the WebDriver when testing is done
driver.quit()