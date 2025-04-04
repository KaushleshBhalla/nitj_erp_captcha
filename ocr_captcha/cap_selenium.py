from selenium import webdriver # Importing webdriver
from selenium.webdriver.common.by import By # To get elements
from selenium.webdriver.common.keys import Keys # To press buttons
import time # Importing time module to wait for page load

CAPTCHA_URL = "https://i.ibb.co/3hnBz4f/69670.jpg" # Specifying captcha url

driver = webdriver.Chrome() # Initialising webdriver
driver.get("https://www.google.com/?olud") # Going to google lens upload page

time.sleep(1) # 1 second delay to make sure that the image uploader is available

# Getting the input element by placeholder and sending the captcha url
input_elem = driver.find_element(By.XPATH, '//input[@placeholder="Paste image link"]')
input_elem.send_keys(CAPTCHA_URL)
input_elem.send_keys(Keys.ENTER)

time.sleep(4) # Waiting for the image to get uploaded and scanned

driver.find_element(By.ID, 'text').click() # Going to text tab
time.sleep(2) # Delay to ensure text tab has loaded

driver.find_element(By.XPATH, "//span[contains(text(), 'Select all text')]").click() # Finding select all text button by it's inside text

time.sleep(1) # Minor delay to ensure text load

result = driver.find_element(By.XPATH, '//div[@class="VIH6Y AbOGud "]').find_element(By.TAG_NAME, 'h1').text # Getting result
print(result) # Printing result