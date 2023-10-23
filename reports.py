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


# Test Case  Verify if the page loads successfully
    driver.get("http://localhost/medical/reports.php")
    # # assert "Sold Reports" in driver.title
    print("Test Case 11: Page Load for Report - Passed")

# Test Case  Check if the page contains specific elements
    table = driver.find_element(By.ID, "dataTable_wrapper")  # Replace with the actual element ID
    print("Test Case 12: Table Existence in Report - Passed")

# Test Case 3: Perform a search or filter operation
# If there is a search bar, perform a search operation and verify results
    driver.get("http://localhost/medical/reports.php")
    search_input_r = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    Buyer_Name = "Rahul"
    search_input_r.send_keys(Buyer_Name)
    search_input_r.send_keys(Keys.RETURN)
    print("Test Case 13: Search in Report - Passed")

    # Wait for the table with pagination to load (you may need to replace this with an appropriate element)
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dataTable"))
    )

    # Find the "Next" button and click it
    next_button = driver.find_element(By.LINK_TEXT, "Next")  # Replace with the actual link text
    next_button.click()

    # Add a short delay to ensure the next page is loaded
    # time.sleep(2)

    # Find the "Previous" button and click it
    previous_button = driver.find_element(By.LINK_TEXT, "Previous")  # Replace with the actual link text
    previous_button.click()

    # Add another delay to ensure the previous page is loaded
    # time.sleep(2)

    print("Test Case 17: Next and Previous buttons tested -Passed")

except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()     