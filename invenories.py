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

    driver.get("http://localhost/medical/inventeries.php")
    # Wait for DataTable to initialize
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "dataTable_wrapper")))

    # Test searching
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
    Product_name = "colfin syrup"
    search_input.send_keys(Product_name)
    search_input.send_keys(Keys.RETURN)

    # Verify that the table contains filtered results
    table = driver.find_element(By.ID, "dataTable")
    rows = table.find_elements(By.TAG_NAME, "tr")
    # The number of rows should be greater than 1 if there are search results
    assert len(rows) > 1, "Search results not found."
    print("Test Case 9: Search the Product in inventory- Passed", Product_name)



     # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dataTable"))
    )
    # driver.get("http://localhost/medical/inventeries.php")
    # # Replace 'Your Category Name' with the actual category name you want to select
    # # category_name = 'Other'

    # # Find the link to select the category and click it
    # category_link = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/a[2]/div')
    # category_link.click()

    # print("Selected category: ")


#     # Define the item to delete (you may need to locate the item in your DataTable)
#     item_to_delete = "acetaminophen"  # Replace with the actual item name
# # Locate and click the delete button for the specified item (adjust locators as needed)
#     delete_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Item")
#     delete_button.click()
#     print("Test Case 10: Deleted Product in inventory- Passed")

except Exception as e:
    print(f"An error occurred: {str(e)}")
# Close the WebDriver
driver.quit()    