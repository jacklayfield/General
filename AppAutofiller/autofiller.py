from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize a WebDriver instance (assuming Chrome)
driver = webdriver.Chrome()

# Navigate to the login page
login_url = "https://markelcorp.wd5.myworkdayjobs.com/en-US/GlobalCareers/login?redirect=%2Fen-US%2FGlobalCareers%2FuserHome"
driver.get(login_url)

time.sleep(5)

# Find and fill in the login credentials
username_field = driver.find_element(By.ID, "input-4")
password_field = driver.find_element(By.ID, "input-5")

# Replace YourUsername with your actual username
username_field.send_keys("YourUsername")
# Replace YourPassword with your actual password
password_field.send_keys("YourPassword")

time.sleep(1)

sign_in_button = driver.find_element(
    By.XPATH, "//*[@id='wd-Authentication-NO_METADATA_ID-uid6']/div/div[1]/div/form/div[3]/div/div/div/div/div")
sign_in_button.click()

time.sleep(3)


driver.quit()
