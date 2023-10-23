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

        # Navigate to the billing page
    
    driver.get("http://localhost/medical/inventeries.php")
# Select items to add to the bill by finding buttons with specific text
    select_buttons = driver.find_elements(By.XPATH, '//*[@id="selection1"]/button')
    for select_button in select_buttons:
        select_button.click()
        
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    view_bill_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bill"]/a[1]/button')))
    view_bill_button.click()
    driver.get("http://localhost/medical/billing.php")
    # Click the "View Bill" button in the modal to calculate the total bill
    view_bill_modal_button = driver.find_element(By.ID, "View Bill")  # Replace with the actual ID
    view_bill_modal_button.click()


# Fill out the purchaser information form in the modal using ID or Name attributes
    name_input = driver.find_element(By.NAME, "name")  
    contact_input = driver.find_element(By.NAME, "contact")  
    discount_input = driver.find_element(By.NAME, "discount")  

    name_input.send_keys("Arya1")
    contact_input.send_keys("785-4568-7890")
    discount_input.send_keys("7 ")  # Optional: Adjust the discount value
    view_bill_modal_button = driver.find_element(By.NAME, "billInfo")  # Replace with the actual ID
# or
    # view_bill_modal_button = driver.find_element(By.NAME, "billInfoButton")  # Replace with the actual Name
    view_bill_modal_button.click()

    print("Test Case 14: View Bill- Passed")
except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()        