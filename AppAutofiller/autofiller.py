from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize a WebDriver instance (assuming Chrome)
driver = webdriver.Chrome()

# Navigate to the login page
login_url = "https://myurl"
driver.get(login_url)

# Find and fill in the login credentials
username_field = driver.find_element_by_id("input-4")
password_field = driver.find_element_by_id("input-5")

# Replace YourUsername with your actual username
username_field.send_keys("YourUsername")
# Replace YourPassword with your actual password
password_field.send_keys("YourPassword")

driver.quit()
